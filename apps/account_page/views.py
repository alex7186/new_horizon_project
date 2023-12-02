from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from apps.account_page.models import AccountTestProgress, Profile
from apps.test_progress.models import Test

from apps.main.scripts import register_user_activity


@login_required()
@register_user_activity
def view_account_page(request):

    context = {"tests_list": []}

    user_profile = Profile.objects.get(user_id=request.user.pk)

    for test_progress in AccountTestProgress.objects.filter(profile=user_profile.pk):

        test = list(Test.objects.filter(id=test_progress.id))[0]

        if test_progress.current_status == 0:
            current_status = "Не начато"
        elif test_progress.current_status == 1:
            current_status = "В процессе"
        elif test_progress.current_status == 2:
            current_status = "Завершено"

        context["tests_list"].append(
            {
                "header_text": test.header_text,
                "detailed_text": test.detailed_text,
                "type": test.type,
                "result": min(15, test_progress.result * 100),
                "current_status": current_status,
            }
        )

    return render(request, "account_page.html", context)
