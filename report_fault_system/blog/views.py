import json
from io import BytesIO
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import UserForm
from tool.captcha import Captcha
from repository.models import User, Blog, Direction, Classification


def home_demo(request, **kwargs):
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
        # 文章列表

        # 提取浏览器中的cookie，如果不为空，表示已经登录
        username = request.COOKIES.get('username')
        # session = list(request.session.values())
        # 是否已开通博客
        user = blog_opening = None
        if username:
            user = User.objects.filter(username=username).first()
            blog_opening = hasattr(user, 'blog')

        return render(request, 'blog/home_demo.html',
                      {
                          'user_form': user_form,
                          'username': username,
                          'user': user,
                          'blog_opening': blog_opening,
                          'classification_choice': classification_choice,
                      }
                      )


def home(request, **kwargs):
    if request.method == 'GET':
        for key, value in kwargs.items():
            kwargs[key] = int(kwargs.pop(key))
    direction_list = Direction.objects.all()

    return render(request, 'blog/home.html',
                  {
                      'direction_list': direction_list,
                  }
                  )


def get_item_set(request):
    id = request.GET.get('id')
    id = int(id)

    direction_obj = Direction.objects.filter(id=id).first()
    classification_list = direction_obj.direction.values_list('name')
    classification_list = list(classification_list)
    classification_list = list(zip(*classification_list))[0]

    ret = json.dumps(classification_list)

    return HttpResponse(ret)


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


def blog_open(request, **kwargs):
    Blog.objects.create(**kwargs)
    return HttpResponseRedirect('/blog/home/')


def my_blog(request, **kwargs):
    return render(request, 'blog/myblog.html', locals())


def test(request):
    return render(request, 'blog/test.html')
