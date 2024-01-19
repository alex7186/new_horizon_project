from django.db import models


class AboutInfo(models.Model):
    title = models.CharField(max_length=100)
    main_text = models.TextField(default="Основной текст")

    class Meta:
        verbose_name = "4.1 Главный текст"
        verbose_name_plural = "4.1 Главный текст"
