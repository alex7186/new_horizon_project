from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from apps.account_page.models import AccountTestProgress, Profile
from apps.test_progress.models import TestObject

from apps.main.scripts import register_user_activity


@login_required()
@register_user_activity
def view_account_page(request):

    context = {"tests_list": []}

    user_profile = Profile.objects.get(user_id=request.user.pk)

    for test_progress in AccountTestProgress.objects.filter(profile=user_profile.pk):

        test = list(TestObject.objects.filter(pk=test_progress.test))

        # if test_progress.current_status == 0:
        #     current_status = "Не начато"
        # elif test_progress.current_status == 1:
        #     current_status = "В процессе"
        # elif test_progress.current_status == 2:
        #     current_status = "Завершено"

        context["tests_list"].append(
            {
                "header_text": test.test_object_name,
                # "type": test.type,
                # "result": min(15, test_progress.result * 100),
                # "current_status": current_status,
            }
        )

    return render(request, "account_page.html", context)
