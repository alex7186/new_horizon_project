from django.shortcuts import render
from modules.projects.models import Project
from modules.popular_element.models import PopularArticle, PopularProject
from modules.main.models import PosterDescription, MainDescription

from modules.main.views import UserVisistor

# import logging
# logger = logging.getLogger('logger')


def project_index(request):
    projects = Project.objects.all()
    poster_description = PosterDescription.objects.all()
    main_description = MainDescription.objects.all()

    popular_projects = []
    for popular_projet in PopularProject.objects.all():
        if popular_projet.enabled:
            popular_projects.append(popular_projet.projects.all())

    popular_articles = []
    for popular_article in PopularArticle.objects.all():
        if popular_article.enabled:
            popular_articles.append(popular_article.articles.all())

    context = {
        "projects": projects,
        "popular_articles": popular_articles,
        "poster_description": poster_description,
        "main_description": main_description,
    }

    UserVisistor(request=request)

    return render(request, "project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)
