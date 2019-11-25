from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import UserForm


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
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
        return HttpResponse('....')
    else:
        return HttpResponse('++++++++')
