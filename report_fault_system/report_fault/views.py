from django.shortcuts import render, redirect, reverse, HttpResponse
from repository.models import Trouble
from .troubleform import TroubleForm


def home(request):
    troubles = Trouble.objects.all()
    return render(request, 'report_fault/home.html',
                  {
                      'troubles': troubles,
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
