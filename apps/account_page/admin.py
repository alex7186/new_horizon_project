from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from apps.account_page.models import Profile, AccountTestProgress
from apps.test_progress.models import TestObject

from misc.admin_styling_components import (
    show_user_profile_card,
    show_linker_block,
    show_test_block,
    arange_block_box,
)


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile
    max_num = 1
    can_delete = False


# @admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def show_linked_user(self):
        profile = Profile.objects.filter(user=self).first()

        return show_user_profile_card(user=profile.user)

    show_linked_user.short_description = "Пользователь 👇"

    list_display = (show_linked_user,)

    inlines = (ProfileInlineAdmin,)


@admin.register(AccountTestProgress)
class AccountTestProgressAdmin(admin.ModelAdmin):
    def show_linked_user(self, obj):

        return show_user_profile_card(user=obj.profile.all().first().user)

    show_linked_user.short_description = "Пользователь 👇"

    def show_connection(self, obj):
        return show_linker_block(linker=obj)

    show_connection.short_description = mark_safe("Связывающий<br>объект 👇")

    def show_test(self, obj):

        res = []
        for test in list(TestObject.objects.filter(id=obj.id)):

            res.append(show_test_block(test))

        return arange_block_box(elements=res)

    show_test.short_description = "Название теста 👇"

    list_display = (
        "show_linked_user",
        "show_connection",
        "show_test",
    )


admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
