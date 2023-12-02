from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.contrib import admin

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

        return mark_safe(
            f"""<div style="background-color: #353535;display: inline-block;
            padding:5px;font-size: 75%;font-weight: 700; margin-bottom:5px;
            line-height: 1;text-align: left;min-width:50px;border-left:5px solid yellow;
            width: 350px;min-height: 50px;
            vertical-align: baseline;border-radius:5px;font-size: 12px;">
            <a href="/admin/articles/article/{obj.pk}/change/"
            style="color:white;font-size:14px;padding:0px;">{obj.pk} - {obj.title}</a>
            </div><br>"""
        )

    show_title.short_description = "Название 👇"

    def show_flag_article_enabled(self, obj):

        color = "green" if obj.flag_article_enabled else "red"
        text = "Да" if obj.flag_article_enabled else "Нет"

        return mark_safe(
            f"""<div style="background-color: {color};display: inline-block;
            padding: .25em .4em;font-size: 75%;font-weight: 700; margin-bottom:5px;
            line-height: 1;text-align: center;white-space: nowrap;min-width:50px;
            vertical-align: baseline;border-radius: .25rem;font-size: 12px;">{text}</div>"""
        )

    show_flag_article_enabled.short_description = "Показывается"

    def show_categories(self, obj):
        res = []

        for category in obj.categories.all():
            res.append(
                f"""<div style="background-color: {category.color};display: inline-block;
                padding:5px;font-size: 75%;font-weight: 700; margin-bottom:5px;
                line-height: 1;text-align: center;white-space: nowrap;border-left:5px solid yellow;
                vertical-align: baseline;border-radius:5px;font-size: 12px;">
                <a style="color:white" href="/admin/articles/category/{category.pk}/change/">
                {category.name}</a></div><br>"""
            )

        return mark_safe(" ".join(res))

    show_categories.short_description = "Категории 👇"

    def show_edited_created_time(self, obj):

        return mark_safe(
            f"""<p style="padding:0px;margin:0px">
            {obj.last_modified.strftime("%H:%M")}</p>
            <p style="padding:0px;margin:0px">
            {obj.last_modified.strftime("%d.%m.%Y")}</p>
            """
        )

    show_edited_created_time.short_description = "Изменено"

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

        return mark_safe(
            f"""<div style="background-color: {headers_count_color};display: inline-block;
            padding: .25em .4em;font-size: 75%;font-weight: 700; margin-bottom:5px;
            line-height: 1;text-align: center;white-space: nowrap;min-width:50px;
            vertical-align: baseline;border-radius: .25rem;font-size: 12px;">{len(headers)}</div>"""
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

        return mark_safe(
            f"""<div style="background-color: {color};display: inline-block;
            padding: .25em .4em;font-size: 75%;font-weight: 700; margin-bottom:5px;
            line-height: 1;text-align: center;white-space: nowrap;min-width:50px;
            vertical-align: baseline;border-radius: .25rem;font-size: 12px;">{articles_count}</div>"""
        )

    show_articles_count.short_description = "Число статей"

    def show_name(self, obj):

        return mark_safe(
            f"""<div style="background-color: #353535;display: inline-block;
            padding:5px;font-size: 75%;font-weight: 700; margin-bottom:5px;
            line-height: 1;text-align: left;min-width:50px;border-left:5px solid yellow;
            width: 350px;min-height: 50px;
            vertical-align: baseline;border-radius:5px;font-size: 12px;">
            <a href="/admin/articles/category/{obj.pk}/change/"
            style="color:white;font-size:14px;padding:0px;">{obj.pk} - {obj.name}</a>
            </div><br>"""
        )

    show_name.short_description = "Название 👇"

    def show_articles(self, obj):
        res = []

        for article in obj.articles.all():
            res.append(
                f"""<div style="background-color: #353535;
                padding:5px;font-size: 75%;font-weight: 700; margin-bottom:5px;
                line-height: 1;text-align: left;min-width:50px;border-left:5px solid yellow;
                width: 350px;
                vertical-align: baseline;border-radius:5px;font-size: 12px;">
                <a href="/admin/articles/article/{article.pk}/change/"
                style="color:white;font-size:14px;padding:0px;">{article.pk} - {article.title}</a>
                </div>"""
            )

        return mark_safe(" ".join(res))

    show_articles.short_description = "Статьи 👇"

    def show_color(self, obj):
        return mark_safe(
            f"""<div style="background-color: {obj.color};display: inline-block;
            padding: .25em .4em;font-size: 75%;font-weight: 700; margin-bottom:5px;
            line-height: 1;text-align: center;white-space: nowrap;min-width:50px;min-height:12px;
            vertical-align: baseline;border-radius: .25rem;font-size: 12px;"></div>"""
        )

    show_color.short_description = "Цвет"

    form = CategoryForm

    list_display = (
        "show_name",
        "show_articles_count",
        "show_color",
        "show_articles",
    )

    search_fields = ("name",)
