from django.contrib import admin

from django.utils.safestring import mark_safe
from apps.popular_element.models import PopularProject, PopularArticle


# Register your models here.
@admin.action(description="➡️ Включить")
def PopularProject_make_enabled(modeladmin, request, queryset):
    queryset.update(enabled=True)


@admin.action(description="➡️ Выключить")
def PopularProject_make_disabled(modeladmin, request, queryset):
    queryset.update(enabled=False)


@admin.register(PopularProject)
class PopularProjectAdmin(admin.ModelAdmin):
    def show_projects(self, obj):
        res = []
        for project in obj.projects.all():
            res.append(f"#{project.pk} - {project.title}")

        res = "<br>".join(res)

        return mark_safe(res)

    show_projects.short_description = "Избранные материалы (pk)"

    def show_count(self, obj):
        return str(len(obj.projects.all()))

    show_count.short_description = "Число материалов"

    list_display = (
        "show_projects",
        "enabled",
        "show_count",
    )

    actions = [PopularProject_make_enabled, PopularProject_make_disabled]


@admin.action(description="➡️ Включить")
def PopularArticle_make_enabled(modeladmin, request, queryset):
    queryset.update(enabled=True)


@admin.action(description="➡️ Выключить")
def PopularArticle_make_disabled(modeladmin, request, queryset):
    queryset.update(enabled=False)


@admin.register(PopularArticle)
class PopularArticleAdmin(admin.ModelAdmin):
    def show_artcles(self, obj):
        res = []
        for artcle in obj.articles.all():
            res.append(f"#{artcle.pk} - {artcle.title}")

        res = "<br>".join(res)

        return mark_safe(res)

    show_artcles.short_description = "Избранные статьи (pk)"

    # def show_enabled
    def show_count(self, obj):
        return str(len(obj.articles.all()))

    show_count.short_description = "Число материалов"

    list_display = (
        "show_artcles",
        "enabled",
        "show_count",
    )

    actions = [PopularArticle_make_enabled, PopularArticle_make_disabled]
