import json
from django.db import connection
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.db.models import Q
from repository.models import Trouble, User
from .troubleform import TroubleForm
from blog.forms import UserForm


def home(request):
    user_form = UserForm()
    troubles = Trouble.objects.all()
    return render(request, 'report_fault/home.html',
                  {
                      'troubles': troubles,
                      'user_form': user_form,
                  })


def get_trouble(request, **kwargs):
    trouble_id = int(kwargs.get('trouble_id', 0))
    if request.method == 'GET':
        trouble_form = TroubleForm()
    else:
        trouble_form = TroubleForm(request.POST)
        if trouble_form.is_valid():
            ret = trouble_form.save(trouble_id)
            if ret:
                return redirect('/report_fault/home/')
            else:
                return HttpResponse('处理中的单子无法操作')
    return render(request, 'report_fault/get_trouble.html',
                  {
                      'trouble_form': trouble_form,
                  })


def set_trouble(request, **kwargs):
    id = kwargs.get('trouble_id')
    id = int(id)

    obj = Trouble.objects.filter(id=id, status=1).values('title', 'user', 'detail', 'ctime')
    obj = list(obj)[0]

    trouble_form = TroubleForm(obj)
    return render(request, 'report_fault/get_trouble.html',
                  {
                      'trouble_form': trouble_form,
                      'id': id
                  })


def del_trouble(request, **kwargs):
    trouble_id = int(kwargs.get('trouble_id'))
    Trouble.objects.filter(id=trouble_id, status__in=(1, 3)).delete()

    return redirect(reverse('report_fault_home'))


def rob_trouble(request, **kwargs):
    trouble_id = int(kwargs.get('trouble_id'))
    num = Trouble.objects.filter(Q(id=trouble_id) | Q(status=1)).update(status=2)
    if not num:
        return HttpResponse('手速太慢，抢单失败')
    return redirect(reverse('report_fault_home'))


def report_trouble(request):
    # sql = '''
    # SELECT strftime('%s', ctime) ,
    # (SELECT count(id) FROM main.Trouble as T2 WHERE processor_id=1 AND T1.ctime=T2.ctime),
    # (SELECT count(id) FROM main.Trouble as T2 WHERE processor_id=2 AND T1.ctime=T2.ctime)
    # FROM main.Trouble as T1 GROUP BY strftime('%Y-%m', ctime);
    # '''
    return render(request, 'report_fault/report_trouble.html')


def report_trouble_get(request):
    cursor = connection.cursor()
    series_data = list()
    user_list = User.objects.all()
    for user in user_list:
        cursor.execute(
            '''SELECT strftime('%%s', strftime('%%Y-%%m-01', ctime)) * 1000, count(id) FROM main.Trouble WHERE processor_id=%s GROUP BY strftime('%%Y-%%m', ctime)''',
            [user.id, ])
        result = cursor.fetchall()
        if result:
            dic = {
                'name': user.username,
                'data': result,
            }
            series_data.append(dic)
    return HttpResponse(json.dumps(series_data))
