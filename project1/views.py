from django.shortcuts import render, redirect
from django.contrib import messages
from project1.forms import DatastoreForm
from project1.models import datastore  # Note: lowercase 'd'

def create_student(request):
    if request.method == "POST":
        form = DatastoreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully!')
            return redirect('create_student')
    else:
        form = DatastoreForm()
    
    return render(request, 'projects/creat.html', {'form': form})


def view_student(request):
    students = datastore.objects.all().order_by("id")

    if request.method == "POST":
        form = DatastoreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect("view-student")   # ✅ Correct
    else:
        form = DatastoreForm()

    return render(request, "projects/view.html", {
        "form": form,
        "students": students,
    })





def delete_student(request, id):
    student = datastore.objects.get(id=id)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Deleted successfully!")
        return redirect("view-student")

    return render(request, "projects/delete.html", {"student": student})
