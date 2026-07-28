from django.urls import path
from home.views import home, Json_data, project_list, project_create, project_update, project_delete,dashboard

urlpatterns = [
    path('data/', home),
    path('json/', Json_data),
    path('project-list/', project_list,name="list"),
    path('project-create/', project_create, name="project-create"),
    path('project-update/<int:id>/', project_update,name="update"),
    path('project-delete/', project_delete,name="delete"), 
    path('dashboard/', dashboard, name='dashboard'),
    
]

