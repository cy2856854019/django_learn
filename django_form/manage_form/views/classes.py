from django.shortcuts import render, redirect
from manage_form import models, myform


def get(request):
    cls_list = models.Class.objects.all()
    return render(request, 'get_class.html', {'cls_list': cls_list})


def add(request):
    if request.method == "GET":
        form = myform.ClassForm()
        return render(request, 'add_class.html', {'form': form})
    elif request.method == "POST":
        form = myform.ClassForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            teacher_list = form.cleaned_data.pop('teacher')
            obj = models.Class.objects.create(**form.cleaned_data)
            obj.teacher.set(teacher_list)
            return redirect('/manage_form/class/get/')
        else:
            return render(request, 'add_class.html', {'form': form})


def delete_class(request):
    class_id = request.GET.get('class_id')
    models.Student.objects.filter(Class_id=class_id).delete()
    models.Class.objects.filter(id=class_id).delete()
    return redirect('/app1/get_class')


def edit_class(request):
    if request.method == "GET":
        class_id = request.GET.get('class_id')
        cls = models.Class.objects.filter(id=class_id).first()
        return render(request, 'edit_class.html', {'cls': cls})
    elif request.method == "POST":
        # class_id = request.POST.get('class_id')
        # class_name = request.POST.get('class_name')
        # models.Class.objects.filter(id=class_id).update(class_name=class_name)
        # return redirect('/app1/get_class')
        class_id = request.GET.get('class_id')
        class_name = request.POST.get('class_name')
        models.Class.objects.filter(id=class_id).update(class_name=class_name)
        return redirect('/app1/get_class')


def set_class_teacher(request):
    if request.method == "GET":
        class_id = request.GET.get('class_id')
        teacher_list = models.Class.objects.filter(id=class_id).first().teacher.all()
        all_teacher_list = models.Teacher.objects.all()
        return render(request, 'set_class_teacher.html', {
            'teacher_list': teacher_list,
            'all_teacher_list': all_teacher_list,
            'class_id': class_id,
        })
    elif request.method == "POST":
        class_id = request.GET.get('class_id')
        class_teacher_id_list = request.POST.getlist('class_teacher_id')
        print('class_id: {}, class_teacher_id_list: {}'.format(class_id, class_teacher_id_list))

        models.Class.objects.filter(id=class_id).first().teacher.set(class_teacher_id_list)

        return redirect('/app1/get_class')
