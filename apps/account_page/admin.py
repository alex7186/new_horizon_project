from django.contrib import admin

from datetime import datetime
import pandas as pd

from apps.account_page.models import (
    Profile,
    InterfaceDownloadUsersList,
    InterfaceUploadUsersList,
)
from apps.account_page.admin_filters import IsAdminFilter

from misc.admin_styling_components import (
    show_user_profile_card,
    show_load_excel_block,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def show_linked_user(self):
        # profile = Profile.objects.get(pk=self.pk)

        return show_user_profile_card(profile=self)

    show_linked_user.short_description = "Пользователь 👇"

    # fields = ("email", "first_name", "last_name", "password", "is_superuser", "groups")

    exclude = ()

    list_display = (show_linked_user,)

    list_filter = (IsAdminFilter,)


@admin.register(InterfaceDownloadUsersList)
class InterfaceDownloadUsersListAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def has_add_permission(self, request, obj=None):
        return False

    @admin.action(description="Сформировать выгрузку")
    def generate_file(modeladmin, request, queryset):
        # queryset.update(flag_article_enabled=False)
        res = []
        for profile in Profile.objects.filter(is_admin=False):
            res.append(
                [
                    profile.user.email,
                    profile.user.first_name,
                    profile.user.last_name,
                    profile.user.password,
                ]
            )

        pd.DataFrame(res, columns=["Почта", "Имя", "Фамилия", "Пароль"]).to_excel(
            f"/root/new_horizon_project/static/files/users.xlsx",
            index=False,
        )

        InterfaceDownloadUsersList.objects.first().last_used_at = datetime.now()
        InterfaceDownloadUsersList.objects.first().save()

    def show_download_element(self, obj):
        return show_load_excel_block(obj)

    show_download_element.short_description = ""

    def show_download_settings(self, obj):
        return ""

    show_download_settings.short_description = ""

    list_display = (
        "show_download_settings",
        "show_download_element",
    )

    readonly_fields = ("last_used_at",)

    actions = (generate_file,)


@admin.register(InterfaceUploadUsersList)
class InterfaceUploadUsersListAdmin(admin.ModelAdmin):
    def show_upload_element(self, obj):
        return show_load_excel_block(obj, show_link=False)

    show_upload_element.short_description = ""

    list_display = ("show_upload_element",)

    readonly_fields = ("last_used_at",)

    # def has_add_permission(self, request, obj=None):
    #     return False


# admin.site.unregister(User)
# admin.site.unregister(Group)
# admin.site.register(User, UserAdmin)
