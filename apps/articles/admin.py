from cgitb import enable
from django.contrib import admin
from apps.articles.models import Article, Category, Comment
from apps.projects.models import Project

from django.utils.safestring import mark_safe


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    def show_title(self, obj):
        res = f'<p style="font-size:15px;">#{obj.pk} {obj.title}</p>'

        return mark_safe(res)

    show_title.short_description = "Название 👇"

    def show_categories(self, obj):
        res = []

        for category in obj.categories.all():
            res.append(
                '<p style="background-color:#264b5d;'
                + 'padding:5px;margin:5px;"><a href="'
                + f'/admin/articles/category/{category.pk}/change/">'
                + f"{category.name}</a></p>"
            )

        res = " ".join(res)

        return mark_safe(res)

    show_categories.short_description = "Категории 👇"

    def show_edited_created_time(self, obj):
        res = "".join(
            (
                "<p>E " + obj.last_modified.strftime("%Y.%m.%d %H:%M:%S") + "</p>",
                "<p>C " + obj.created_on.strftime("%Y.%m.%d %H:%M:%S") + "</p>",
            )
        )

        return mark_safe(res)

    show_edited_created_time.short_description = "Изменено/Создано"

    def show_main_text_headers_list(self, obj):
        headers = [
            f'<a href="/articles/{obj.pk}#queried_header{i+1}">➡️ {header}</a>'
            for i, header in enumerate(obj.main_text_headers_list)
        ]

        delimiter = 1

        main_delimited = len(headers) // delimiter

        exceed_number = 5
        max_count_exceeded = main_delimited > exceed_number

        res = ""
        for i in range(main_delimited):
            if max_count_exceeded and i > 4:
                continue

            headirs_indicated_dict = dict(
                zip(
                    range(i, i + delimiter),
                    headers[i * delimiter : (i + 1) * delimiter],
                )
            )
            for index, element in headirs_indicated_dict.items():
                current_pk = (index + 1) + i * (delimiter - 1)
                res += "".join(f"#{current_pk} {element} ")

            res += "<br>"

        if (main_delimited) > 0 and not max_count_exceeded:
            headirs_indicated_dict = dict(
                zip(
                    range(delimiter * (main_delimited), len(headers)),
                    headers[delimiter * (main_delimited) : len(headers)],
                )
            )

            for index, element in headirs_indicated_dict.items():
                res += "".join([f"#{(index + 1)} {element} "])
            res = res[:-2]

        elif not max_count_exceeded:
            res = res[:-6]

        elif max_count_exceeded:
            res += f"<p>+ {len(headers) - exceed_number}<p>"

        if not headers:
            res = (
                '<p style="background-color:red;'
                + "padding:5px;margin:5px;width:170px;"
                + "text-align:center;font-size:15px;"
                + 'height:20px;padding:5px;">'
                + "НЕТ</p>"
            )

        return mark_safe(res)

    show_main_text_headers_list.short_description = "Подзаголовки 👇"

    def show_count_of_mentions(self, obj):
        mentions = []
        res = []

        for project in Project.objects.all():
            current_article_link = f"/articles/{obj.pk}/"
            if current_article_link in project.article_inner_links:
                mentions.append((project.pk, project.title))

        for mention in mentions:
            res.append(
                f'<a style="padding:5px;margin:5px;'
                + "font-size:15px;"
                + "margin-left:0px;padding-left:0px;"
                + 'height:20px;padding:5px;"'
                + f' href="/{mention[0]}"'
                + f">➡️ {mention[1]}</a>"
            )

        if len(res) == 0:
            res.append(
                f'<p style="padding:5px;margin:5px;'
                + "background-color:red;"
                + "text-align:center;font-size:15px;"
                + 'height:20px;padding:5px;"'
                + f">НЕТ</p>"
            )

        res = "<br>".join(res)

        return mark_safe(res)

    show_count_of_mentions.short_description = "Упоминания 👇"

    def show_main_text_headers_list_keys(self, obj):
        return mark_safe(
            "<br>".join(obj.main_text_headers_list_keys.replace(",", " ").split())
        )

    show_main_text_headers_list_keys.short_description = "Ключевые слова"
    list_display = (
        "show_title",
        "show_categories",
        "show_edited_created_time",
        "show_main_text_headers_list",
        "show_count_of_mentions",
        "show_main_text_headers_list_keys",
    )

    list_filter = (
        "created_on",
        "last_modified",
    )

    search_fields = (
        "title",
        "attractive_text",
        "main_text",
    )

    readonly_fields = ("main_text_headers_list",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def show_articles_count(self, obj):
        articles_count = len(obj.articles.all())

        obj.articles_count = articles_count

        color = "green" if articles_count > 3 else "red"
        if articles_count < 2:
            warnig_msg = " (слишком мало)"
            color = "red"
        elif articles_count < 3:
            warnig_msg = " (мало)"
            color = "orange"
        elif 3 <= articles_count < 7:
            warnig_msg = " (нормально)"
            color = "green"
        else:
            warnig_msg = " (слишком много)"
            color = "purple"

        res = (
            ""
            + f'<p style="background-color:{color};'
            + "padding:5px;margin:5px;width:150px;"
            + f'text-align:center;font-size:15px;">'
            + f"{articles_count}{warnig_msg}"
            + "</p>"
        )

        obj._show_articles_count = res

        return mark_safe(res)

    show_articles_count.short_description = "Число статей по категории"
    # show_articles_count.admin_order_field = "articles_count"

    def show_name(self, obj):
        res = f'<p style="font-size:15px;">#{obj.pk} {obj.name}</p>'

        return mark_safe(res)

    show_name.short_description = "Название 👇"

    def show_articles(self, obj):
        res = []

        for article in obj.articles.all():
            res.append(
                '<p style="background-color:#264b5d;'
                + "max-width:400px;"  # + "font-size:15px;" \
                + 'padding:5px;margin:5px;"><a href="'
                + f'/admin/articles/article/{article.pk}/change/">➡️ #{article.pk} {article.title}</a></p>'
            )

        res = " ".join(res)

        return mark_safe(res)

    show_articles.short_description = "Статьи 👇"

    list_display = (
        "show_name",
        "show_articles_count",
        "show_articles",
    )

    search_fields = ("name",)


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):

#     list_display = (
#         "author",
#         "body",
#         "created_on",
#         "article",
#     )
