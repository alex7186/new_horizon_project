from django.db import models

# from apps.projects.models import Project
from apps.articles.models import Article, Category


class PopularArticle(models.Model):
    title = models.CharField(max_length=40, default="")
    articles = models.ManyToManyField(Article)
    enabled = models.BooleanField(default=False)

    class Meta:
        verbose_name = "5.1. Группа 'Избранные статьи'"
        verbose_name_plural = "5.1. Группы 'Избранные статьи'"


class CategoriesTiles(models.Model):
    title = models.CharField(max_length=40, default="")
    categories = models.ManyToManyField(Category, related_name="tiles")
    enabled = models.BooleanField(default=False)

    class Meta:
        verbose_name = "5.2. Группа 'Плитки с категориями'"
        verbose_name_plural = "5.2. Группы 'Плитки с категориями'"
