from django.contrib import admin

from apps.popular_element.models import PopularArticle

from misc.admin_supprotive_blocks import show_data_colored_badge
from misc.admin_styling_components import (
    show_data_colored_border_block,
    arange_block_box,
)


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
                show_data_colored_border_block(
                    link_href=f"/admin/articles/article/{article.pk}/change/",
                    text=article.title,
                    color="yellow",
                    text_bold=True,
                )
            )

        # return mark_safe(" ".join(res))

        return arange_block_box(elements=res, max_width=500)

    show_artcles.short_description = "Статьи 👇"

    def show_enabled(self, obj):

        color = "green" if obj.enabled else "red"
        text = "Да" if obj.enabled else "Нет"

        return show_data_colored_badge(color=color, text=text, text_bold=True)

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
