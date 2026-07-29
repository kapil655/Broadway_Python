from urllib import request

from django.shortcuts import redirect, render
from . import models
from .forms import StudentForms, GradeForm
from user.models import UserImage
from django.contrib.auth.decorators import login_required


# =========================
# STUDENT CRUD
# =========================

def student_list(request):
    data = models.Student.objects.all()

    context = {
        "student": data
    }

    return render(request, "student/index.html", context)


def student_create(request):
    form = StudentForms()

    if request.method == "POST":
        form = StudentForms(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student")

    context = {
        "form": form
    }

    return render(request, "student/create.html", context)


def student_update(request, id):
    student = models.Student.objects.get(id=id)

    form = StudentForms(instance=student)

    if request.method == "POST":
        form = StudentForms(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("student")

    context = {
        "form": form
    }

    return render(request, "student/update.html", context)


def student_delete(request, id):
    student = models.Student.objects.get(id=id)

    if request.method == "POST":
        student.delete()
        return redirect("student")

    context = {
        "student": student
    }

    return render(request, "student/delete.html", context)




# GRADE CRUD
@login_required(login_url='/user/login')
def grade_list(request):
    data = models.Grade.objects.all()
    context = {
        "grade": data
    }
    return render(request, "grade/index.html", context)


@login_required(login_url='/user/login')
def grade_create(request):
    form = GradeForm()
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("grade-list")
    context = {
        "form": form
    }
    return render(request, "grade/create.html", context)


@login_required(login_url='/user/login')
def grade_update(request, id):
    grade = models.Grade.objects.get(id=id)
    form = GradeForm(instance=grade)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect("grade-list")
    context = {
        "form": form
    }
    return render(request, "grade/update.html", context)


@login_required(login_url='/user/login')
def grade_delete(request, id):
    grade = models.Grade.objects.get(id=id)
    if request.method == "POST":
        grade.delete()
        return redirect("grade-list")
    context = {
        "grade": grade
    }
    return render(request, "grade/delete.html", context)
@login_required(login_url='/user/login')
def user_image(request):
    data = UserImage.objects.all()
    context = {"user": data}
    return render(request, "user/index.html", context)







