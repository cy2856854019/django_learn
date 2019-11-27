import json
from io import BytesIO
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm
from tool.captcha import Captcha
from repository.models import User


def home(request, **kwargs):
    if request.method == 'GET':
        for key, value in kwargs.items():
            kwargs[key] = int(kwargs.pop(key))
        classification_choice = (
            (1, 'Python'),
            (2, 'Java'),
            (3, 'Php'),
            (4, 'C/C++'),
            (5, 'Node.js'),
        )

        user_form = UserForm()
        # 提取浏览器中的cookie，如果不为空，表示已经登录
        username = request.COOKIES.get('username')
        session = list(request.session.values())
        print(session)

        return render(request, 'blog/home.html', locals())


def login(request):
    current_captcha = request.POST.get('captcha').upper()
    session_captcha = request.session['captcha'].upper()
    if current_captcha != session_captcha:
        return HttpResponse('验证码错误')

    username = request.POST.get('username')
    psw = request.POST.get('psw')

    user = User.objects.filter(username=username, psw=psw)
    if not user:
        return HttpResponse('用户名或密码错误')
    if request.POST.get('save_login'):
        # 如在前端选择了一周内免登录，则设置对应的session有效时间
        request.session.set_expiry(5)
    response = HttpResponseRedirect('/blog/home/')
    # 如果cookie没有设置过期时间，当用户关闭浏览器的时候，cookie就自动过期了。
    response.set_cookie('username', username)
    return response


def login_out(request):
    response = HttpResponseRedirect('/blog/home/')
    response.delete_cookie('username')
    return response


def register(request):
    current_captcha = request.POST.get('captcha').upper()
    session_captcha = request.session['captcha'].upper()
    if current_captcha != session_captcha:
        return HttpResponse('验证码错误')

    user_form = UserForm(request.POST)
    if user_form.is_valid():
        ret = user_form.save()
        if not ret:
            # 用户名已存在
            return HttpResponse('用户名已存在')
        return HttpResponse('注册成功')
    return HttpResponse(str(user_form.errors))


def get_check_code(request):
    img, code = Captcha().generate_captcha()
    request.session['captcha'] = code

    fb = BytesIO()
    img.save(fb, 'png')
    return HttpResponse(fb.getvalue())
