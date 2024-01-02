from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from apps.account_page.models import AccountTestProgress, Profile
from apps.test_progress.models import TestObject

from apps.main.scripts import register_user_activity

from misc.template_styling_components import show_test_result_card

from django.utils.safestring import mark_safe
import sys


@login_required()
@register_user_activity
def view_account_page(request):

    context = {"tests_list": []}
    res = []

    user_profile = Profile.objects.get(user_id=request.user.pk)

    for test_progress in AccountTestProgress.objects.filter(profile=user_profile.pk):

        res.append(
            show_test_result_card(
                test=test_progress.tests.first(),
                test_progress=test_progress,
            )
        )

        # {
        #     "header_text": test.get("test_object_name"),
        #     "test_required_result": test.get("test_required_result"),
        #     "test_max_result": test.get("test_max_result"),
        #     "test_type": test.get("test_type"),
        #     "current_status": test_progress.current_status,
        #     "result": test_progress.result,
        # }

    # print(f"{res=}", file=sys.stdout)
    context["tests_list"] = mark_safe(
        '<div style="margin-top:45px;">' + "".join(res) + "</div>"
    )

    return render(request, "account_page.html", context)
