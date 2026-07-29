from django.urls import path
from home.views import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('list/', ProjectListView.as_view(), name="project-list"),
    path('create/', ProjectCreateView.as_view(), name="project-create"),
    path('update/<int:pk>/', ProjectUpdateView.as_view(), name="project-update"),
]