from django.db import models

# from apps.projects.models import Project
from apps.articles.models import Article


class PopularArticle(models.Model):
    articles = models.ManyToManyField(Article)
    title = models.CharField(max_length=40, default="")
    enabled = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Группа статей"
        verbose_name_plural = "Группа статей"
