from django.urls import path
from apps.projects import views

urlpatterns = [
    path("", views.project_index, name="home"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
