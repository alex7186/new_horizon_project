from django.db import models


class AboutInfo(models.Model):
    title = models.CharField(max_length=100)
    main_text = models.TextField(default="Основной текст")


class MainDescription(models.Model):
    description_text = models.TextField(default="Текст краткого описания сервиса")


class PosterDescription(models.Model):
    main_poster_text = models.TextField(default="Основной текст постера")
    main_poster_secondary_text = models.TextField(
        default="Второстепенный текст постера"
    )
