from django.shortcuts import render, redirect, HttpResponse
from django.core import serializers
from RedisTools import myRedis
from ca_redis.models import Terminal


# Create your views here.
def ca_set(request):
    if request.method == 'GET':
        terminals = Terminal.objects.all().values('id', 'name', 'available_ports')
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


def get_available_port(request):
    id = request.GET.get('id')
    terminal = Terminal.objects.filter(id=id)
    terminal = serializers.serialize('json', terminal)

    return HttpResponse(terminal)
