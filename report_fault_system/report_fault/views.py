from django.shortcuts import render


def home(request):
    return render(request, 'report_fault/home.html')
