# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404
from django.views import generic

import os

from apps.main.scripts import register_user_activity
from apps.main.models import AboutInfo, ExcelFile

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


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if not os.path.exists(file_path):
        raise Http404

    with open(file_path, "rb") as file_object:
        response = HttpResponse(
            file_object.read(), content_type="application/vnd.ms-excel"
        )
        response["Content-Disposition"] = "inline; filename=" + os.path.basename(
            file_path
        )
        return response


class CsvDownloadView(generic.ListView):

    model = ExcelFile
    fields = ["file"]
    template_name = "download.html"


class CsvUploadView(generic.CreateView):

    model = ExcelFile
    fields = ["file"]
    template_name = "upload.html"


def err404(request, exception):
    return render(request, "404.html", status=404)


def err500(request):
    return render(request, "404.html", status=404)
