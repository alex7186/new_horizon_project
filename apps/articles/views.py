import urllib

from django.shortcuts import render

from apps.articles.models import Article, Category


from apps.main.scripts import register_user_activity
from apps.popular_element.models import CategoriesTiles


@register_user_activity
def articles_index(request):
    articles = Article.objects.filter(flag_article_enabled=True).order_by(
        "-last_modified"
    )

    category_tiles_object = CategoriesTiles.objects.first()
    category_tiles_list = category_tiles_object.categories.all()

    context = {
        "articles": articles,
        "category_tiles": category_tiles_list,
        "category_tiles_title": category_tiles_object.title,
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
