from django.shortcuts import render, redirect
from manage_form import models, myform


def get(request):
    teacher_list = models.Teacher.objects.all()
    return render(request, 'get_teacher.html', {'teacher_list': teacher_list})


def add(request):
    if request.method == 'GET':
        form = myform.TeacherForm()
        return render(request, 'add_teacher.html', {'form': form})
    elif request.method == 'POST':
        form = myform.TeacherForm(request.POST)
        # 一定要先调用is_valid方法
        if form.is_valid():
            models.Teacher.objects.update_or_create(**form.cleaned_data)
            return redirect('/manage_form/teacher/get/')
        else:
            return render(request, 'add_teacher.html', {'form': form})


def delete(request):
    id = request.GET.get('id')
    models.Teacher.objects.filter(id=id).delete()
    return redirect('/manage_form/teacher/get')


def edit(request):
    if request.method == "GET":
        id = request.GET.get('id')
        teacher = models.Teacher.objects.get(id=id)

        form = myform.TeacherForm({
            'name': teacher.name,
            'age': teacher.age,
            'gender': teacher.gender,
        })

        return render(request, 'edit_teacher.html', {'form': form})
    elif request.method == "POST":
        form = myform.TeacherForm(request.POST)
        # 一定要先调用is_valid方法
        if form.is_valid():
            models.Teacher.objects.update(**form.cleaned_data)
            return redirect('/manage_form/teacher/get/')
        else:
            return render(request, 'edit_teacher.html', {'form': form})
