import os
import json
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

    direction_list = myadmin_models.Direction.objects.all()
    if condition.get('direction_id'):
        # 筛选出当前方向下的分类
        classification_list = myadmin_models.Direction.objects.filter(
            id=condition['direction_id']).first().classification.all()
        # 筛选出当前方向下的分类的id
        classification_id_list = myadmin_models.Direction.objects.get(
            id=condition['direction_id']).classification.values_list('id')
        classification_id_list = list(zip(*classification_id_list))[0]
        '''
        当classification_id为空时,筛选当前方向下所有分类
        不为空时,判断当前的classification_id是否在当前分类里,
        不在分类里,跳至全部分类
        '''
        if not condition.get('classification_id'):
            condition['classification_id__in'] = classification_id_list
        else:
            if condition.get('classification_id') not in classification_id_list:
                kwargs['classification_id'] = 0
        # 删除掉direction_id
        condition.pop('direction_id')
    else:
        classification_list = myadmin_models.Classification.objects.all()
    level_list = myadmin_models.Level.objects.all()
    status_list = list(map(lambda x: {'key': x[0], 'value': x[1]}, myadmin_models.Video.status_choice))
    video_list = myadmin_models.Video.objects.filter(**condition)
    print(condition)
    return render(request, 'video2.html',
                  {
                      'direction_list': direction_list,
                      'classification_list': classification_list,
                      'level_list': level_list,
                      'status_list': status_list,
                      'kwargs': kwargs,
                      'video_list': video_list,
                  })


def img_video(request):
    img_list = myadmin_models.ImgVideo.objects.all()
    return render(request, 'img_video.html',
                  {
                      'img_list': img_list,
                      # 'MEDIA_URL': MEDIA_URL,
                  })


def img_video2(request):
    return render(request, 'img_video2.html')


def get_img(request):
    img_video_list = list(myadmin_models.ImgVideo.objects.values('id', 'img_path','title', 'summary'))
    ret = {
        'status': True,
        'data': img_video_list,
    }
    ret = json.dumps(ret)
    return HttpResponse(ret)


def get_pdf(request):
    print(request.method)
    print(request.POST)
    print(request.FILES)

    file_obj = request.FILES.get('file')
    filename = os.path.join(r'D:\Pycharm_DCG\virtual\django\official_web_demo\static', file_obj.name)
    print(file_obj, file_obj.name)
    with open(filename, 'wb') as fp:
        for i in file_obj.chunks():
            fp.write(i)

    return HttpResponse('...')
