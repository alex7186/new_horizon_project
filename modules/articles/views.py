import urllib

from django.shortcuts import render

# from articles.forms import CommentForm
# from articles.models import Comment
from modules.articles.models import Article, Category

from modules.popular_element.models import PopularProject

from rest_framework import generics
from modules.articles.serializers import (
    ArticlePreviewSerializer,
    CategorySerializer,
    ArticleSerializer,
)

from modules.main.views import UserVisistor


def articles_index(request):
    popular_projects = []
    for popular_projet in PopularProject.objects.all():
        if popular_projet.enabled:
            popular_projects.append(popular_projet.projects.all())

    articles = Article.objects.all().order_by("-created_on")
    context = {
        "articles": articles,
        "popular_projects": popular_projects,
    }

    UserVisistor(request=request)

    return render(request, "articles_index.html", context)


def articles_category(request, category):
    category_decoded = urllib.parse.unquote(category)

    articles = Article.objects.filter(
        categories__name__contains=category_decoded
    ).order_by("-created_on")
    context = {"category": category_decoded, "articles": articles}

    UserVisistor(request=request)

    return render(request, "articles_category.html", context)


def articles_detail(request, pk):
    article = Article.objects.get(pk=pk)
    # comments = Comment.objects.filter(article=article)

    # form = CommentForm()
    # if request.method == "POST":
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = Comment(
    #             author=form.cleaned_data["author"],
    #             body=form.cleaned_data["body"],
    #             article=article,
    #         )
    #         comment.save()

    context = {
        "article": article,
        # "comments": comments,
        # "form": form,
        "keys": article.main_text_headers_list_keys,
    }

    UserVisistor(request=request)

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
