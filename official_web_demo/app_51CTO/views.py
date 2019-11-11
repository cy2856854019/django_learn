import os
from django.shortcuts import render, HttpResponse
from myadmin import models as myadmin_models


def video(request, **kwargs):
    condition = dict()
    for k, v in kwargs.items():
        kwargs[k] = int(v)
        if int(v) == 0:
            continue
        condition[k] = int(v)
    direction_list = myadmin_models.Direction.objects.all()
    classification_list = myadmin_models.Classification.objects.all()
    level_list = myadmin_models.Level.objects.all()
    status_list = list(map(lambda x: {'key': x[0], 'value': x[1]}, myadmin_models.Video.status_choice))

    video_list = myadmin_models.Video.objects.filter(**condition)
    return render(request, 'video.html',
                  {
                      'direction_list': direction_list,
                      'classification_list': classification_list,
                      'level_list': level_list,
                      'status_list': status_list,
                      'kwargs': kwargs,
                      'video_list': video_list,
                  })


def video2(request, **kwargs):
    condition = dict()
    for k, v in kwargs.items():
        kwargs[k] = int(v)
        if int(v) == 0:
            continue
        condition[k] = int(v)
    if condition.get('direction_id'):
        direction_list = myadmin_models.Direction.objects.all()
        classification_list = myadmin_models.Direction.objects.get(id=condition['direction_id']).classification.all()
    else:
        classification_list = myadmin_models.Classification.objects.all()
        if condition.get('classification_id'):
            direction_list = myadmin_models.Classification.objects.get(
                id=condition['classification_id']).direction_set.all()
        else:
            direction_list = myadmin_models.Direction.objects.all()
    level_list = myadmin_models.Level.objects.all()
    status_list = list(map(lambda x: {'key': x[0], 'value': x[1]}, myadmin_models.Video.status_choice))

    print(condition)
    video_list = myadmin_models.Video.objects.filter(**condition)
    return render(request, 'video2.html',
                  {
                      'direction_list': direction_list,
                      'classification_list': classification_list,
                      'level_list': level_list,
                      'status_list': status_list,
                      'kwargs': kwargs,
                      'video_list': video_list,
                  })


def get_pdf(request):
    print(request.method)
    print(request.POST)
    print(request.FILES)

    file_obj = request.FILES.get('file')
    print(file_obj, file_obj.name)
    filename = os.path.join(r'D:\Pycharm_DCG\virtual\django\official_web_demo\static', file_obj.name)
    with open(filename, 'wb') as fp:
        for i in file_obj.chunks():
            fp.write(i)

    return HttpResponse('...')
