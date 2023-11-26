# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import auth

from apps.main.scripts import register_user_activity
from apps.main.models import AboutInfo

from apps.popular_element.models import PopularArticle


@register_user_activity
def main_page(request):

    popular_articles = []
    for popular_article in PopularArticle.objects.all():
        if popular_article.enabled:
            popular_articles.append(
                popular_article.articles.filter(flag_article_enabled=True)
            )

    about_info = AboutInfo.objects.all()
    # poster_description = PosterDescription.objects.all()

    # for popular_projet in popular_projects:
    #     print('popular_projects', popular_projet, popular_projet.projects, dir(popular_projet.projects))
    context = {
        "popular_articles": popular_articles,
        "about_info": about_info,
    }

    return render(request, "main_page.html", context)

# def logout(request):
#     auth.logout(request)
#     return main_page(request)


def err404(request, exception):
    return render(request, "404.html", status=404)


def err500(request):
    return render(request, "404.html", status=404)
