from django.contrib import admin

from apps.main.models import AboutInfo

from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def has_add_permission(self, request, obj=None):
        return False

    def show_main_text(self, obj):
        if len(obj.main_text) > 150:
            return mark_safe(obj.main_text[:150] + " ...")

        return mark_safe(obj.main_text[:150])

    show_main_text.short_description = "Текст раздела"

    def show_main_text_len(self, obj):
        return len(obj.main_text)

    show_main_text_len.short_description = "Длинна текста"

    def show_title(self, obj):
        return obj.title

    show_title.short_description = "Заголовок"

    list_display = (
        "show_title",
        "show_main_text",
        "show_main_text_len",
    )
