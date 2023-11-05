from django.db import models

# from apps.projects.models import Project
from apps.articles.models import Article


# Create your models here.
# class PopularProject(models.Model):
#     projects = models.ManyToManyField(Project)
#     enabled = models.BooleanField(default=False)


class PopularArticle(models.Model):
    articles = models.ManyToManyField(Article)
    enabled = models.BooleanField(default=False)
