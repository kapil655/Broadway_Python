from django.urls import path
from .views import (
    DashboardView,
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    LoginView,
)

urlpatterns = [
    path("list/", UserListView.as_view(), name="list"),
    path("create/", UserCreateView.as_view(), name="create"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="delete"),
    path("dashboard/", DashboardView.as_view(), name="Dashboard"),
    path("login/", LoginView.as_view(), name="login")


]