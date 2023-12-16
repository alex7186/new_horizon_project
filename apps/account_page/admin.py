from django.contrib import admin
from apps.account_page.models import Profile, AccountTestProgress
from apps.test_progress.models import Test
from django.utils.safestring import mark_safe


from misc.admin_styling_components import show_user_profile_card


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def show_linked_user(self, obj):

        return show_user_profile_card(user=obj.user)

    show_linked_user.short_description = "Пользователь 👇"

    def show_linked_test_progress(self, obj):

        res = []

        for test_progress in list(AccountTestProgress.objects.filter(profile=obj.pk)):
            test = Test.objects.get(id=test_progress.id)

            if test.type == 1:
                test_result = f"""
                <div style="border:1px solid #808080;widht:100%;
                height:20px;margin-bottom:5px;margin-top:5px;border-radius:5px">
                    <div style="text-align:center;background-color:
                    {'green' if test_progress.result > 0.3 else 'red'};
                    width:{max(5, int(test_progress.result*100))}%;
                    height:100%;border-radius:5px"></div>
                </div>
                """

            if test.type == 2:
                test_result = f"""
                <div style="border:1px solid #808080;widht:100%;
                height:20px;margin-bottom:5px;margin-top:5px;border-radius:5px">
                    <div style="background-color:{'green' if test_progress.result > 0.5 else 'red'};
                    width:100%;height:100%;border-radius:5px;text-align:center;
                    color:white;font-size: 15px;">
                    {'Пройдено' if test_progress.result > 0.3 else 'Не пройдено'}</div>
                </div>
                """

            if test_progress.current_status == 0:
                current_status = "Не начато"
            elif test_progress.current_status == 1:
                current_status = "В процессе"
            elif test_progress.current_status == 2:
                current_status = "Завершено"

            text = f"""
                <div style="width:250px;>
                    <div style="">#{test.pk} {test.header_text}</div>
                    <div style="font-size:10px;margin-top:5px;">{test.detailed_text}</div>
                    <div style="margin-top:15px;">{current_status}</div>
                    {test_result}
                </div>
                """

            res.append(
                f"""<div style="background-color: #353535;width:350px;
                color:white;font-size:14px!important;padding:0px;display: inline-block;
                padding: .25em .4em;font-size: 75%;font-weight: 700; margin-bottom:10px;
                line-height: 1;text-align: left;min-width:50px;
                border-radius: .25rem;font-size: 12px;display: flow-root;">
                {text}</div>
                """
            )

        return mark_safe(" ".join(res))

    show_linked_test_progress.short_description = "Прогресс тестов"

    list_display = (
        "show_linked_user",
        "show_linked_test_progress",
    )


@admin.register(AccountTestProgress)
class AccountTestAdmin(admin.ModelAdmin):
    def show_linked_test_progress(self, obj):

        test = list(obj.tests.all())[0]

        if test.type == 1:
            test_result = f"""
            <div style="border:1px solid #808080;widht:100%;
            height:20px;margin-bottom:5px;margin-top:5px;border-radius:5px">
                <div style="text-align:center;background-color:
                {'green' if obj.result > 0.3 else 'red'};
                width:{max(5, int(obj.result*100))}%;
                height:100%;border-radius:5px"></div>
            </div>
            """

        if test.type == 2:
            test_result = f"""
            <div style="border:1px solid #808080;widht:100%;
            height:20px;margin-bottom:5px;margin-top:5px;border-radius:5px">
                <div style="background-color:{'green' if obj.result > 0.5 else 'red'};
                width:100%;height:100%;border-radius:5px;text-align:center;
                color:white;font-size: 15px;">
                {'Пройдено' if obj.result > 0.3 else 'Не пройдено'}</div>
            </div>
            """

        if obj.current_status == 0:
            current_status = "Не начато"
        elif obj.current_status == 1:
            current_status = "В процессе"
        elif obj.current_status == 2:
            current_status = "Завершено"

        text = f"""
            <div style="width:250px;>
                <div style="">#{test.pk} {test.header_text}</div>
                <div style="font-size:10px;margin-top:5px;">{test.detailed_text}</div>
                <div style="margin-top:15px;">{current_status}</div>
                {test_result}
            </div>
            """

        res = f"""<div style="background-color: #353535;width:350px;
            color:white;font-size:14px!important;padding:0px;display: inline-block;
            padding: .25em .4em;font-size: 75%;font-weight: 700; margin-bottom:10px;
            line-height: 1;text-align: left;min-width:50px;
            border-radius: .25rem;font-size: 12px;display: flow-root;">
            {text}</div>
            """

        return mark_safe(res)

    show_linked_test_progress.short_description = "Прогресс тестов"

    def show_linked_user(self, obj):

        return show_user_profile_card(user=list(obj.profile.all())[0].user)

    show_linked_user.short_description = "Пользователь 👇"

    list_display = (
        "show_linked_user",
        "show_linked_test_progress",
    )
