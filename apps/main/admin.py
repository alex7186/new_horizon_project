from django.contrib import admin

from apps.main.models import AboutInfo, PosterDescription, MainDescription

from django.utils.safestring import mark_safe


# Register your models here.
@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    def show_main_text(self, obj):
        if len(obj.main_text) > 150:
            return mark_safe(obj.main_text[:150] + " ...")

        return mark_safe(obj.main_text[:150])

    show_main_text.short_description = "Текст раздела"

    def show_main_text_len(self, obj):
        return len(obj.main_text)

    show_main_text_len.short_description = "Длинна текста (в символах)"

    def show_title(self, obj):
        return obj.title

    show_title.short_description = "Заголовок"

    list_display = (
        "show_title",
        "show_main_text",
        "show_main_text_len",
    )


@admin.register(PosterDescription)
class PosterDescriptionAdmin(admin.ModelAdmin):
    def show_main_poster_text(self, obj):
        return mark_safe(obj.main_poster_text)

    show_main_poster_text.short_description = "Главная часть"

    def show_main_poster_secondary_text(self, obj):
        return mark_safe(obj.main_poster_secondary_text)

    show_main_poster_secondary_text.short_description = "Второстепенная часть"

    list_display = (
        "show_main_poster_text",
        "show_main_poster_secondary_text",
    )


@admin.register(MainDescription)
class MainDescriptionAdmin(admin.ModelAdmin):
    def show_description_text(self, obj):
        return mark_safe(obj.description_text)

    show_description_text.short_description = "Текст раздела"

    def show_text_len(self, obj):
        return len(obj.description_text)

    show_text_len.short_description = "Длинна текста (в символах)"

    list_display = (
        "show_description_text",
        "show_text_len",
    )
