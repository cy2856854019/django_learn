import json
from io import BytesIO
from django.shortcuts import render, HttpResponse, redirect
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
        return render(request, 'blog/home.html', locals())


def login(request):
    if request.method == "POST":
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
            request.session.set_expiry(60 * 60 * 24 * 7)
        return HttpResponse('登录成功')

    else:
        return HttpResponse('+++++++++++')


def register(request):
    if request.method == "POST":
        current_captcha = request.POST.get('captcha').upper()
        session_captcha = request.session['captcha'].upper()
        if current_captcha != session_captcha:
            return HttpResponse('验证码错误')

        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse('....')
        return HttpResponse(str(user_form.errors))
    else:
        return HttpResponse('++++++++')


def get_check_code(request):
    img, code = Captcha().generate_captcha()
    request.session['captcha'] = code

    fb = BytesIO()
    img.save(fb, 'png')
    return HttpResponse(fb.getvalue())
