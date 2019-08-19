from django.shortcuts import render, HttpResponse
import json


def ajax1(request):
    if request.method == 'GET':
        return render(request, 'ajax_demo/ajax1.html')
    else:
        url = request.POST.get('url')
        print(request.GET)
        ret = {'url': url}
        return HttpResponse(json.dumps(ret))
