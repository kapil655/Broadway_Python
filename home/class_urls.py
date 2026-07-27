from django.urls import path
from home.views import ProjectListView

urlpatterns = [
    path('list',ProjectListView.as_view(), name="project-list")

]