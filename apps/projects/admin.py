from django.contrib import admin

from django.utils.safestring import mark_safe

from apps.projects.models import Project

from apps.articles.models import Article


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def show_title(self, obj):
        res = f'<p style="font-size:15px;">#{obj.pk} {obj.title}</p>'

        return mark_safe(res)

    show_title.short_description = "Название 👇"

    def show_article_inner_links(self, obj):

        articles_pks = []
        articles_titles = []
        for article in Article.objects.all():
            articles_pks.append(article.pk)
            articles_titles.append(article.title)

        articles_pk_titles = dict(zip(articles_pks, articles_titles))

        links = []
        # print(articles_pk_titles)
        for link in obj.article_inner_links:

            pk = [el for el in link.split("/") if el][1]
            pk = int(pk)

            links.append(
                '<p style="'
                + "padding:0px;margin:0px;"
                + '"><a href="'
                + f"/admin/articles/article/{pk}/change/"
                + f'">#{int(pk)} {articles_pk_titles[int(pk)]}</a></p>'
            )

        res = "".join(links)

        if not links:
            res = (
                ""
                + '<p style="background-color:red;font-size:15px;'
                + 'height:20px;padding:5px;">НЕТ</p>'
            )

        return mark_safe(res)

    show_article_inner_links.short_description = "Ссылки на статьи 👇"

    def show_edited_created_time(self, obj):
        res = "".join(
            (
                '<p style="padding:0px;">'
                + obj.last_modified.strftime("%H:%M %d.%m.%Y")
                + "</p>",
                '<p style="padding:0px;">'
                + obj.created_on.strftime("%H:%M %d.%m.%Y")
                + "</p>",
            )
        )

        return mark_safe(res)

    show_edited_created_time.short_description = "Изменено/Создано"

    list_display = (
        "show_title",
        "show_edited_created_time",
        "show_article_inner_links",
    )

    search_fields = (
        "title",
        "attractive_text",
        "main_text",
    )

    # list_filter = (
    #     "created_on",
    #     "last_modified",
    # )

    readonly_fields = ("article_inner_links",)
