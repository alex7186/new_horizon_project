from django.contrib import admin

from django.utils.safestring import mark_safe
from apps.popular_element.models import PopularArticle


@admin.register(PopularArticle)
class PopularArticleAdmin(admin.ModelAdmin):
    @admin.action(description="➡️ Включить")
    def PopularArticle_make_enabled(modeladmin, request, queryset):
        queryset.update(enabled=True)

    @admin.action(description="➡️ Выключить")
    def PopularArticle_make_disabled(modeladmin, request, queryset):
        queryset.update(enabled=False)

    def show_artcles(self, obj):
        res = []
        for article in obj.articles.all():

            res.append(
                f"""<div style="background-color: #353535;display: inline-block;
                padding: .25em .4em;font-size: 75%;font-weight: 700; margin-bottom:5px;
                line-height: 1;text-align: left;min-width:50px;border-left:5px solid yellow;
                vertical-align: baseline;border-radius: .25rem;font-size: 12px;"><a 
                href="/admin/articles/article/{article.pk}/change/"
                style="color:white;font-size:14px;padding:0px;">{article.pk} - {article.title}</a></div><br>"""
            )

        return mark_safe(" ".join(res))

    show_artcles.short_description = "Избранные статьи (pk)"

    def show_enabled(self, obj):

        color = "green" if obj.enabled else "red"
        text = "Да" if obj.enabled else "Нет"

        return mark_safe(
            f"""<div style="background-color: {color};display: inline-block;
            padding: .25em .4em;font-size: 75%;font-weight: 700; margin-bottom:5px;
            line-height: 1;text-align: center;white-space: nowrap;min-width:50px;
            vertical-align: baseline;border-radius: .25rem;font-size: 12px;">{text}</div>"""
        )

    show_enabled.short_description = "Показывается"

    def show_count(self, obj):
        return str(len(obj.articles.all()))

    show_count.short_description = "Число материалов"

    list_display = (
        "show_artcles",
        "show_enabled",
        "show_count",
    )

    actions = [PopularArticle_make_enabled, PopularArticle_make_disabled]
