from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from home.forms import ProjectForm
from home.models import Project
from django.views.generic.list import ListView

def home(request):
    data = request.GET
    name = data.get('name', 'default')
    return HttpResponse(name)

def Json_data(request):
    data = {
        "name": "kapil",
        "age": 34,
    }
    return JsonResponse(data)



def project_list(request):
    data = Project.objects.all()
    context = {
        "project": data
    }
    return render(request, 'projects/index.html', context)




def project_create(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/project-list/')  
    
    context = {
        "form": form
    }
    return render(request, 'projects/create2.html', context)




def project_update(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)
    
    if request.method == "POST":
        form = ProjectForm(data=request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/home/project-list/') 
    
    context = {
        "form": form,
        "project": project
    }
    return render(request, 'projects/update.html', context)




def project_delete(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('/home/project-list/')  


def dashboard(request):
    return render(request, 'base/dashboard.html')

# class based views
class ProjectListView(ListView):
    model = Project
    template_name ='projects/index.html'
    context_object_name = "project"

# home/project_list.html
# <app:name>/<modelname_list>.html


    
