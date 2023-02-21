# -*- coding: utf-8 -*-

from django.shortcuts import render

from apps.main.scripts import register_user_activity
from apps.main.models import AboutInfo, PosterDescription


@register_user_activity
def about_page(request):
    about_info = AboutInfo.objects.all()
    poster_description = PosterDescription.objects.all()

    context = {
        "about_info": about_info,
        "poster_description": poster_description,
    }

    return render(request, "about.html", context)


def err404(request, exception):
    return render(request, "404.html", status=404)


def err500(request):
    return render(request, "404.html", status=404)
