# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import auth

from apps.main.scripts import register_user_activity
from apps.main.models import AboutInfo

from apps.popular_element.models import PopularArticle, CategoriesTiles


@register_user_activity
def main_page(request):

    popular_article_object = PopularArticle.objects.first()
    popular_articles_list = (
        popular_article_object.articles.filter(flag_article_enabled=True)
        if popular_article_object.enabled
        else []
    )

    category_tiles_object = CategoriesTiles.objects.first()
    category_tiles_list = category_tiles_object.categories.all()

    about_info = AboutInfo.objects.all()

    context = {
        "popular_articles": popular_articles_list,
        "popular_articles_title": popular_article_object.title,
        "category_tiles": category_tiles_list,
        "category_tiles_title": category_tiles_object.title,
        # "popular_articles": PopularArticle.objects.all(),
        "about_info": about_info,
    }

    return render(request, "main_page.html", context)


def err404(request, exception):
    return render(request, "404.html", status=404)


def err500(request):
    return render(request, "404.html", status=404)
