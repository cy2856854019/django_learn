import json
from io import BytesIO
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import UserForm
from tool.captcha import Captcha


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
    pass


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
