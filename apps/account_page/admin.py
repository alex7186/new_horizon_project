from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.safestring import mark_safe

from apps.account_page.models import Profile, AccountTestProgress
from apps.account_page.forms import AccountTestProgressFormAdmin
from apps.test_progress.models import TestObject

from misc.admin_styling_components import (
    show_user_profile_card,
    show_linker_block,
    show_test_block,
    arange_block_box,
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


@admin.register(AccountTestProgress)
class AccountTestProgressAdmin(admin.ModelAdmin):
    def show_linked_user(self, obj):

        return show_user_profile_card(profile=obj.profile.first())

    show_linked_user.short_description = "Пользователь 👇"

    def show_connection(self, obj):
        return show_linker_block(linker=obj)

    show_connection.short_description = mark_safe("Связывающий объект 👇")

    def show_test(self, obj):

        return arange_block_box(elements=(show_test_block(obj.tests.first()),))

    show_test.short_description = "Название теста 👇"

    form = AccountTestProgressFormAdmin

    list_display = (
        "show_linked_user",
        "show_connection",
        "show_test",
    )


# admin.site.unregister(User)
# admin.site.unregister(Group)
# admin.site.register(User, UserAdmin)
