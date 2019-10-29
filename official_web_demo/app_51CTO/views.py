from django.shortcuts import render
from myadmin import models as myadmin_models


def video(request, **kwargs):
    condition = dict()
    for k, v in kwargs.items():
        kwargs[k] = int(v)
        if int(v) == 0:
            continue
        condition[k] = int(v)
    classification_list = myadmin_models.Classification.objects.all()
    level_list = myadmin_models.Level.objects.all()
    status_list = list(map(lambda x: {'key': x[0], 'value': x[1]}, myadmin_models.Video.status_choice))

    video_list = myadmin_models.Video.objects.filter(**condition)
    return render(request, 'video.html',
                  {
                      'classification_list': classification_list,
                      'level_list': level_list,
                      'status_list': status_list,
                      'kwargs': kwargs,
                      'video_list': video_list,
                  })
