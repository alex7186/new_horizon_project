from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.contrib import admin

from misc.admin_styling_components import (
    show_data_colored_block,
    show_data_colored_badge,
    show_data_colored_border_block,
    arange_block_box,
)

from apps.articles.models import Article, Category
from apps.articles.forms import CategoryForm


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    @admin.action(description="Показывать статьи")
    def make_arcicle_enabled(modeladmin, request, queryset):
        queryset.update(flag_article_enabled=True)

    @admin.action(description="Скрыть статьи")
    def make_arcicle_disabled(modeladmin, request, queryset):
        queryset.update(flag_article_enabled=False)

    def show_title(self, obj):

        return show_data_colored_border_block(
            text=obj.title,
            text_bold=True,
            color="yellow",
            link_href=f"/admin/articles/article/{obj.pk}/change/",
        )

    show_title.short_description = "Название 👇"

    def show_flag_article_enabled(self, obj):

        color = "green" if obj.flag_article_enabled else "red"
        text = "Да" if obj.flag_article_enabled else "Нет"

        return show_data_colored_badge(text=text, color=color, text_bold=True)

    show_flag_article_enabled.short_description = "Показывается"

    def show_categories(self, obj):
        res = []

        for category in obj.categories.all():

            res.append(
                show_data_colored_block(
                    text=category.name,
                    text_bold=True,
                    color=category.color,
                    link_href=f"/admin/articles/category/{category.pk}/change/",
                )
            )
        return arange_block_box(elements=res)

    show_categories.short_description = "Категории 👇"

    def show_edited_created_time(self, obj):

        return mark_safe(
            f"""<p style="padding:0px;margin:0px">
            {obj.last_modified.strftime("%H:%M")}</p>
            <p style="padding:0px;margin:0px">
            {obj.last_modified.strftime("%d.%m.%Y")}</p>
            """
        )

    show_edited_created_time.short_description = mark_safe("Дата<br>изменения")

    def image_tag(self, obj):

        img_show_tag = f'<img src="{escape(obj.image_base.url)}" style="height:60px"/>'
        img_show_desc = f"""
            <p style="padding:0px; margin:0px;border-top-right-radius: 10px;
            padding-right: 2px;padding-top: 2px;display: inline-flex;font-size:14px;
            background: gray;display: inline-flex;position: relative;top: -21px;">
            {obj.image_base.height} x {obj.image_base.width}</p>"""

        return mark_safe(
            '<div style="height:60px;width:120px">'
            + img_show_tag
            + img_show_desc
            + "</div>"
        )

    image_tag.short_description = "Изображение"
    image_tag.allow_tags = True

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

        return show_data_colored_badge(
            color=headers_count_color, text=len(headers), text_bold=True
        )

    show_main_text_headers_list.short_description = mark_safe("Число<br>подзаголовков")

    def show_text_length(self, obj):

        return mark_safe(f"<p>{len(obj.main_text)}</p>")

    show_text_length.short_description = mark_safe("Длинна<br>текста")

    list_display = (
        "show_title",
        "show_flag_article_enabled",
        "show_categories",
        "show_edited_created_time",
        "image_tag",
        "show_main_text_headers_list",
        "show_text_length",
    )

    list_filter = (
        "last_modified",
        "flag_article_enabled",
    )

    search_fields = (
        "title",
        "attractive_text",
        "main_text",
    )

    readonly_fields = (
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

        return show_data_colored_badge(color=color, text=articles_count, text_bold=True)

    show_articles_count.short_description = "Число статей"

    def show_name(self, obj):

        return show_data_colored_block(
            link_href=f"/admin/articles/category/{obj.pk}/change/",
            text_bold=True,
            text=obj.name,
            color=obj.color,
        )

    show_name.short_description = "Название 👇"

    def show_articles(self, obj):
        res = []

        for article in obj.articles.all():
            res.append(
                show_data_colored_border_block(
                    link_href=f"/admin/articles/article/{article.pk}/change/",
                    text=article.title,
                    color="yellow",
                )
            )

        return arange_block_box(elements=res, min_width=250, max_width=450)

    show_articles.short_description = "Статьи 👇"

    form = CategoryForm

    list_display = (
        "show_name",
        "show_articles_count",
        "show_articles",
    )

    search_fields = ("name",)
