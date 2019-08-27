from django.shortcuts import render
from slideshow.models import SlideShow


def show(request):
    slide_show_list = SlideShow.objects.all()
    img_default_path = r'/static/media/'

    return render(request, 'CompanyWeb.html', locals())

