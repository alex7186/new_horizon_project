from django.urls import path
from apps.articles.views import articles_index, articles_detail, articles_category

urlpatterns = [
    path("", articles_index, name="articles_index"),
    path("<int:pk>/", articles_detail, name="articles_detail"),
    path("<category>/", articles_category, name="articles_category"),
]
