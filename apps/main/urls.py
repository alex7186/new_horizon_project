"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('articles/', include('articles.urls'))
"""
from django.contrib import admin
from django.views.static import serve
from django.urls import path, include, re_path
import settings

from apps.projects.views import project_index, project_detail
from apps.main.views import about_page
from apps.articles.views import ArticleAPIView, CategoryAPIView, ArticleByPKAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("<int:pk>/", project_detail, name="project_detail"),
    path("", project_index, name="home"),
    path("articles/", include("apps.articles.urls")),
    path("quiz/", include("apps.quiz.urls")),
    path("about", about_page, name="about"),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("api/v1/articles_list/", ArticleAPIView.as_view()),
    path("api/v1/article_by_pk/<int:pk>/", ArticleByPKAPIView.as_view()),
    path("api/v1/categories_list/", CategoryAPIView.as_view()),
]


handler404 = "apps.main.views.err404"
handler500 = "apps.main.views.err500"
