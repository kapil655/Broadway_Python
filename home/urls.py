from django.urls import path
from home.views import home, Json_data, project_list, project_create, project_update, project_delete

urlpatterns = [
    path('data/', home),
    path('json/', Json_data),
    path('project-list/', project_list),
    path('project-create/', project_create),
    path('project-update/<int:id>/', project_update),
    path('project-delete/<int:id>/', project_delete), 
]

