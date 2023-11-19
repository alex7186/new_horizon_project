from django.db import models

# from apps.projects.models import Project
from apps.articles.models import Article


class PopularArticle(models.Model):
    articles = models.ManyToManyField(Article)
    enabled = models.BooleanField(default=False)
