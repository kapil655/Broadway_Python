from django.shortcuts import redirect, render
from school.forms import StudentForms
from school.models import School,Student

# Create your views here.
def student_list(request):
    data = Student.objects.all()
    context = {
        "student":data
    }
    return render(request,"student/index.html",context)

def student_create(request):
    form = StudentForms()
    if request.method == "POST":
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    context = {
        "form": form
    }
    return render(request, 'student/create.html', context)


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForms(instance=student)
    if request.method == "POST":
        form = StudentForms(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
    context = {
        "form": form    }
    return render(request, 'student/update.html', context)  


#delete model 

from django.shortcuts import get_object_or_404, redirect, render

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("student")

    context = {
        "student": student
    }

    return render(request, "student/delete.html", context)