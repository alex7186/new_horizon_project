from django.urls import path
from apps.articles import views

urlpatterns = [
    path("", views.articles_index, name="articles_index"),
    path("<int:pk>/", views.articles_detail, name="articles_detail"),
    path("<category>/", views.articles_category, name="articles_category"),
]
