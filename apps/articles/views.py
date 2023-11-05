import urllib

from django.shortcuts import render

from apps.articles.models import Article, Category


from rest_framework import generics
from apps.articles.serializers import (
    ArticlePreviewSerializer,
    CategorySerializer,
    ArticleSerializer,
)

from apps.main.scripts import register_user_activity


@register_user_activity
def articles_index(request):
    articles = Article.objects.filter(flag_article_enabled=True).order_by(
        "-last_modified"
    )
    context = {
        "articles": articles,
    }

    return render(request, "articles_index.html", context)


@register_user_activity
def articles_category(request, category):

    category_decoded = urllib.parse.unquote(category)

    articles = Article.objects.filter(
        categories__name__contains=category_decoded, flag_article_enabled=True
    ).order_by("-last_modified")

    category_object = Category.objects.get(name=category)
    context = {"category": category_object, "articles": articles}

    return render(request, "articles_category.html", context)


@register_user_activity
def articles_detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        "article": article,
        "keys": article.main_text_headers_list_keys,
    }

    return render(request, "articles_detail.html", context)


class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlePreviewSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleByPKAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(pk=self.kwargs["pk"])
        return queryset
