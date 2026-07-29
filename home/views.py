from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from home.forms import ProjectForm
from home.models import Project
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='/user/login')
def project_list(request):
    data = Project.objects.all()
    context = {
        "project": data
    }
    return render(request, 'projects/index.html', context)



@login_required(login_url='/user/login')
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



@login_required(login_url='/user/login')
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



@login_required(login_url='/user/login')
def project_delete(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('project-list/')  


@login_required(login_url='/user/login')
def dashboard(request):
    return render(request, 'base/dashboard.html')

# class based views
# home/project_list.html
# <app:name>/<modelname_list>.html



class ProjectListView(ListView):
    model = Project
    context_object_name = "project"
    template_name ='projects/index.html' # <app:name>/<modelname_list>.html
     # by default : objects_list



class ProjectCreateView(CreateView):
    model = Project
    #fields = ['name','email','start_date']
    form_class = ProjectForm
    template_name = "projects/create2.html" # <app:name>/<modelname_form>.html
    success_url = '/project/list'


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/update.html"
    success_url = '/project/list'
    context_object_name = "form"



class ProjectDeleteView(DeleteView):
    model = Project
    # model.delete()
    # template_name = 'projects/confirm_delete.html'
    # context_object_name = 'project'
    #TypeError: Model.delete() missing 1 required positional argument: 'self'