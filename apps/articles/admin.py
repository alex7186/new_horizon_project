from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.contrib import admin

from apps.articles.models import Article, Category, Comment
from apps.articles.forms import CategoryForm


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    def show_title(self, obj):
        res = f'<p style="font-size:14px;padding:0px;">{obj.pk} - {obj.title}</p>'

        return mark_safe(res)

    show_title.short_description = "Название 👇"

    def show_categories(self, obj):
        res = []

        for category in obj.categories.all():
            res.append(
                "<div"
                + ' class="badge badge-primary"'
                + f' style="background-color: {category.color};padding:3px; margin-top:5px";'
                + f'><a style="color:white" href="/admin/articles/category/{category.pk}/change/">{category.name}</a></div>'
            )

        res = " ".join(res)

        return mark_safe(res)

    show_categories.short_description = "Категории 👇"

    def show_edited_created_time(self, obj):

        return mark_safe(
            '<p style="padding:0px;margin:0px">{}</p>'.format(
                obj.last_modified.strftime("%d.%m.%Y %H:%M")
            )
        )

    show_edited_created_time.short_description = "Изменено"

    def show_main_text_headers_list(self, obj):
        headers = [
            f'{i+1}) <a style="font-size:14px;" href="/articles/{obj.pk}#queried_header{i+1}">{header}</a>'
            for i, header in enumerate(obj.main_text_headers_list)
        ]

        if len(headers) == 0:
            headers_count_color = "red"
        elif len(headers) < 3:
            headers_count_color = "orange"
        elif len(headers) < 6:
            headers_count_color = "green"
        else:
            headers_count_color = "red"

        return mark_safe(
            f'<p style="padding:0px;margin:5px;'
            + f"background-color:{headers_count_color};width: 50px;"
            + "margin-right: auto;"
            + "text-align:center;font-size:15px;"
            + 'height:20px;border-radius:25px;"'
            + f">{len(headers)}</p>"
        )

    show_main_text_headers_list.short_description = "Подзаголовки"

    # def show_count_of_mentions(self, obj):
    #     mentions = []
    #     res = []

    #     for project in Project.objects.all():
    #         current_article_link = f"/articles/{obj.pk}/"
    #         if current_article_link in project.article_inner_links:
    #             mentions.append((project.pk, project.title))

    #     for i, mention in enumerate(mentions):
    #         res.append(
    #             f'{1+i}) <a style="padding:0px;margin:0px;'
    #             + "font-size:14px;"
    #             + 'height:20px;"'
    #             + f' href="/{mention[0]}"'
    #             + f">{mention[1]}</a>"
    #         )

    #     if len(res) == 0:
    #         res.append(
    #             f'<p style="padding:0px;margin:5px;'
    #             + "background-color:red;width: 100px;"
    #             + "margin-right: auto;"
    #             + "text-align:center;font-size:15px;"
    #             + 'height:20px;border-radius:25px;"'
    #             + f">НЕТ</p>"
    #         )

    #     res = "<br>".join(res)

    #     return mark_safe(res)

    # show_count_of_mentions.short_description = "Упоминания 👇"

    # def show_main_text_headers_list_keys(self, obj):
    #     res = []

    #     for i, element in enumerate(obj.main_text_headers_list_keys.split(",")):
    #         res.append(f"{i+1}) {element}<br>")

    #     res[-1] = res[-1][:-4]

    #     return mark_safe(" ".join(res))

    # show_main_text_headers_list_keys.short_description = "Ключевые слова"

    def image_tag(self, obj):

        return mark_safe(
            f'<p style="padding:0px; margin:0px">{obj.image_base.name}</p>'
            + f'<img src="{escape("/static" + obj.image_base.url)}" style="height:60px"/>'
            + f'<p style="padding:0px; margin:0px">{obj.image_base.height} x {obj.image_base.width}</p'
        )

    image_tag.short_description = "Image"
    image_tag.allow_tags = True

    def show_text_length(self, obj):

        return mark_safe(f"<p>{len(obj.main_text)}</p>")

    show_text_length.short_description = "Длинна текста"

    def show_flag_article_enabled(self, obj):

        return mark_safe(
            f'<p style="padding:0px;margin:5px;'
            + f"background-color:{'green' if obj.flag_article_enabled else 'red'};width: 50px;"
            + "margin-right: auto;"
            + "text-align:center;font-size:15px;"
            + 'height:20px;border-radius:25px;"'
            + f">{'Да' if obj.flag_article_enabled else 'Нет'}</p>"
        )

        return mark_safe()

    show_flag_article_enabled.short_description = "Показывается"

    @admin.action(description="Показывать статьи")
    def make_arcicle_enabled(modeladmin, request, queryset):
        for obj in queryset:
            obj.flag_article_enabled = True
            obj.save()

    @admin.action(description="Скрыть статьи")
    def make_arcicle_disabled(modeladmin, request, queryset):
        for obj in queryset:
            obj.flag_article_enabled = False
            obj.save()

    list_display = (
        "show_title",
        "show_flag_article_enabled",
        "show_categories",
        "show_edited_created_time",
        "image_tag",
        "show_main_text_headers_list",
        "show_text_length"
        # "show_count_of_mentions",
        # "show_main_text_headers_list_keys",
    )

    list_filter = (
        # "show_count_of_mentions",
    )

    search_fields = (
        "title",
        "attractive_text",
        "main_text",
    )

    readonly_fields = (
        "image_tag",
        "main_text_headers_list",
        "main_text_headers_list_keys",
        "flag_article_enabled",
    )

    actions = (
        make_arcicle_enabled,
        make_arcicle_disabled,
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def show_articles_count(self, obj):
        articles_count = len(obj.articles.all())

        obj.articles_count = articles_count

        color = "green" if articles_count > 3 else "red"
        if articles_count < 2:
            color = "red"
        elif articles_count < 3:
            color = "orange"
        elif 3 <= articles_count < 7:
            color = "green"
        else:
            color = "red"

        res = (
            f'<p style="padding:0px;margin:5px;'
            + f"background-color:{color};width: 50px;"
            + "margin-right: auto;"
            + "text-align:center;font-size:15px;"
            + 'height:20px;border-radius:25px;"'
            + f">{articles_count}</p>"
        )

        obj._show_articles_count = res

        return mark_safe(res)

    show_articles_count.short_description = "Число статей"

    def show_name(self, obj):

        return mark_safe(
            '<p style="font-size:14px;padding:0px;">{} - {}</p>'.format(
                obj.pk, obj.name
            )
        )

    show_name.short_description = "Название 👇"

    def show_articles(self, obj):
        res = []

        for article in obj.articles.all():
            res.append(
                f'<a href="/admin/articles/article/{article.pk}/change/"'
                + ' style="font-size:14px;padding:0px;">{} - {}</a><br>'.format(
                    article.pk, article.title
                )
                # '<div'
                # + ' class="badge badge-primary"'
                # + ' style="background-color: #5e5c64;'
                # + 'padding:3px; margin-top:5px";'
                # + '><a style="color:white"'
                # + f'href="/admin/articles/article/{article.pk}/change/">{article.title}</a></div>'
            )

        res = " ".join(res)

        return mark_safe(res)

    show_articles.short_description = "Статьи 👇"

    def show_color(self, obj):
        res = (
            ""
            + '<div style="width:20px;'
            + f"height:20px;background-color:{obj.color};"
            + 'border-radius:20px;border:2px solid grey;"></div>'
        )

        return mark_safe(res)

    show_color.short_description = "Цвет"

    form = CategoryForm

    list_display = ("show_name", "show_articles_count", "show_articles", "show_color")

    search_fields = ("name",)


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):

#     list_display = (
#         "author",
#         "body",
#         "created_on",
#         "article",
#     )
