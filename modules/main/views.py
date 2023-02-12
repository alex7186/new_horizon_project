from django.shortcuts import render

from settings import LOG_FILENAME, LOG_FILEPATH
from modules.main.models import AboutInfo, PosterDescription

import os

from datetime import datetime


def about_page(request):
    about_info = AboutInfo.objects.all()
    poster_description = PosterDescription.objects.all()

    UserVisistor(request=request)

    context = {
        "about_info": about_info,
        "poster_description": poster_description,
    }

    return render(request, "about.html", context)


class UserVisistor:
    user_ip: str
    user_agent: str
    prev_page: str

    def __init__(self, request):
        # getting api
        adress = request.META.get("HTTP_X_FORWARDED_FOR")
        if adress:
            self.user_ip = adress.split(",")[-1].strip()
        else:
            self.user_ip = request.META.get("REMOTE_ADDR")

        # getting browser
        self.user_agent = request.META.get("HTTP_USER_AGENT")

        # getting opened_page
        self.opened = request.path

        # appending log file
        message = (
            "\t".join([datetime.now().strftime("%Y.%m.%d %H:%M:%S"), str(self)]) + "\n"
        )

        # loacal data is not interested
        # if "127.0.0.1" in str(self.user_ip):
        #     return None

        with open(os.path.join(LOG_FILEPATH, LOG_FILENAME), "a") as file:
            file.write(message)

    def __str__(self):
        return f"{self.user_ip}\t{self.user_agent}\t{self.opened}"


def err404(request, exception):
    return render(request, "404.html", status=404)


def err500(request):
    return render(request, "404.html", status=404)
