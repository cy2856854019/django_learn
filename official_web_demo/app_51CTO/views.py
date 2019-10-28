from django.shortcuts import render
from myadmin import models as myadmin_models


def video(request, **kwargs):
    for k, v in kwargs.items():
        kwargs[k] = int(v)
    classification_list = myadmin_models.Classification.objects.all()
    level_list = myadmin_models.Level.objects.all()

    video_list = myadmin_models.Video.objects.filter(**kwargs)
    return render(request, 'video.html',
                  {
                      'classification_list': classification_list,
                      'level_list': level_list,
                      'kwargs': kwargs,
                      'video_list': video_list,
                  })
