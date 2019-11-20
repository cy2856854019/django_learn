import json
from django.http import QueryDict
from django.shortcuts import render, redirect, HttpResponse
from django.core import serializers
from RedisTools import myRedis
from ca_redis.models import Terminal, PortSetting
from ca_redis.CaPortForm import CaPortForm


def ca_set(request):
    if request.method == 'GET':
        terminals = Terminal.objects.values('id', 'name', 'available_ports')
        return render(request, 'ca_redis.html', locals())
    else:
        id = request.POST.get('device_name')
        username = request.POST.get('username')
        port = int(request.POST.get('available_port'))
        # 插入到redis中
        ret = myRedis.set(username, port)
        if ret == -1:
            return HttpResponse('公司名称已存在，请勿重复添加')
        # 更新对应机柜的可用端口列表
        obj = Terminal.objects.filter(id=id)
        available_ports = obj[0].available_ports
        available_ports = eval(available_ports)
        available_ports.remove(port)

        no_available_ports = obj[0].no_available_ports
        no_available_ports = eval(no_available_ports)
        no_available_ports.append(port)

        obj.update(available_ports=str(available_ports), no_available_ports=str(no_available_ports))

        return redirect('/ca_redis/set/')


def port_set(request):
    if request.method == 'POST':
        form_obj = CaPortForm(request.POST)
        if form_obj.is_valid():
            '''
            只有调用调用is_valid函数后才会有clean_data, is_valid -> errors -> full_clean -> self.cleaned_data = {}
            '''
            ret = form_obj.save()
            if not ret[1]:
                return HttpResponse('{} 端口已经被使用'.format(ret[0].port))
            return redirect('/ca_redis/port_set/')
        # 若不符合筛选条件，返回不符合的全部错误原因
        return HttpResponse(form_obj.errors['__all__'])

    port_list = PortSetting.objects.values_list('port')
    port_list = list(port_list)
    port_list = list(zip(*port_list))[0]
    port = sorted(port_list)[-1] + 1

    # 给带有ChoiceField类似的form组件传默认值时, 要按照QueryDict对象的方式构造
    default_dict = QueryDict('port=%s&company_name=请输入公司全称&terminal=1' % str(port))
    form_obj = CaPortForm(default_dict)
    return render(request, 'port_set.html', locals())


def port_get(request):
    port_setting = PortSetting.objects.values('port', 'company_name')
    port_setting = list(port_setting)
    # 按照port升序排列
    port_setting = sorted(port_setting, key=lambda x: x['port'])

    ret = {
        "status": True,
        "data": port_setting,
    }
    # 转成json后通过HttpResponse对象返回
    ret = json.dumps(ret)
    response = HttpResponse(ret)

    return response


def get_available_port(request):
    # django的序列化
    id = request.GET.get('id')
    terminal = Terminal.objects.filter(id=id)
    terminal = serializers.serialize('json', terminal)

    return HttpResponse(terminal)
