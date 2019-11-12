from django.shortcuts import render, redirect
from manage_form import models


def get_student(request):
    student_list = models.Student.objects.all()
    return render(request, 'get_student.html', {'student_list': student_list})


def add_student(request):
    if request.method == 'GET':
        class_list = models.Class.objects.all()
        return render(request, 'add_student.html', {'class_list': class_list})
    elif request.method == "POST":
        name = request.POST.get('student_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        class_id = request.POST.get('class_id')

        models.Student.objects.update_or_create(
            name=name,
            age=age,
            gender=gender,
            Class_id=class_id,
        )
        return redirect('/app1/get_student')


def delete_student(request):
    student_id = request.GET.get('student_id')
    models.Student.objects.filter(id=student_id).delete()
    return redirect('/app1/get_student')


def edit_student(request):
    if request.method == "GET":
        student_id = request.GET.get('student_id')
        student = models.Student.objects.filter(id=student_id).first()
        class_list = models.Class.objects.values('id', 'class_name')
        return render(request, 'edit_student.html', {'student': student, 'class_list': class_list})
    elif request.method == "POST":
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        student_age = request.POST.get('student_age')
        student_gender = request.POST.get('student_gender')
        student_class_id = request.POST.get('student_class_id')

        models.Student.objects.filter(id=student_id).update(
            name=student_name,
            age=student_age,
            gender=student_gender,
            Class_id=student_class_id,
        )

        return redirect('/app1/get_student')
