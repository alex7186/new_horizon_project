from django.contrib import admin

from apps.popular_element.models import PopularArticle, CategoriesTiles

from django.utils.safestring import mark_safe

from misc.admin_supprotive_blocks import (
    show_data_colored_badge,
    show_data_colored_block,
)
from misc.admin_styling_components import (
    show_data_colored_border_block,
    show_categories_tiles_block,
    arange_block_box,
    show_popular_block,
    show_article,
)


@admin.register(PopularArticle)
class PopularArticleAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def has_add_permission(self, request, obj=None):
        return False

    @admin.action(description="➡️ Включить")
    def PopularArticle_make_enabled(modeladmin, request, queryset):
        queryset.update(enabled=True)

    @admin.action(description="➡️ Выключить")
    def PopularArticle_make_disabled(modeladmin, request, queryset):
        queryset.update(enabled=False)

    def show_popular_element(self, obj):
        return show_popular_block(obj)

    show_popular_element.short_description = mark_safe("Группа статей 👇")

    def show_artcles(self, obj):
        res = []
        for article in obj.articles.all():

            res.append(show_article(article))
        return arange_block_box(elements=res, max_width=500)

    show_artcles.short_description = "Статьи 👇"

    list_display = (
        "show_popular_element",
        "show_artcles",
    )

    actions = [PopularArticle_make_enabled, PopularArticle_make_disabled]


@admin.register(CategoriesTiles)
class CategoriesTilesAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def has_add_permission(self, request, obj=None):
        return False

    @admin.action(description="➡️ Включить")
    def CategoriesTiles_make_enabled(modeladmin, request, queryset):
        queryset.update(enabled=True)

    @admin.action(description="➡️ Выключить")
    def CategoriesTiles_make_disabled(modeladmin, request, queryset):
        queryset.update(enabled=False)

    def show_categories_tiles_element(self, obj):
        return show_categories_tiles_block(obj)

    show_categories_tiles_element.short_description = mark_safe("Группа категорий 👇")

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

    list_display = (
        "show_categories_tiles_element",
        "show_categories",
    )

    actions = [CategoriesTiles_make_enabled, CategoriesTiles_make_disabled]
