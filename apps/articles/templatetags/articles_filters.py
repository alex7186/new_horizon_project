from django import template
import time
import sys

register = template.Library()


@register.filter(name="rel_articles")
def rel_articles(article):
    categories = list(article.categories.all())
    rel_articles = []
    for relevant_article in categories[-1].articles.filter(flag_article_enabled=True):
        rel_articles.append(relevant_article)

    rel_articles.remove(article)

    return rel_articles[:3]


@register.filter(name="sort_by_creation_date")
def sort_by_date(articles):
    articles_dict = {}
    for article in articles:
        articles_dict.update({article.pk: time.mktime(article.created_on.timetuple())})

    articles_dict = dict(sorted(articles_dict.items(), key=lambda item: item[1]))

    new_articles_list = []
    for pk in articles_dict.keys():
        for article in articles:
            if article.pk == pk:
                new_articles_list.append(article)

    return new_articles_list[::-1]


@register.filter(name="sort_edited_by_date")
def sort_by_date(articles):
    articles_dict = {}
    for article in articles:
        articles_dict.update(
            {article.pk: time.mktime(article.last_modified.timetuple())}
        )

    articles_dict = dict(sorted(articles_dict.items(), key=lambda item: item[1]))

    new_articles_list = []
    for pk in articles_dict.keys():
        for article in articles:
            if article.pk == pk:
                new_articles_list.append(article)

    return new_articles_list[::-1]


@register.filter(name="categories_count")
def get_categories_count(articles):
    return len(article.categories.all())
