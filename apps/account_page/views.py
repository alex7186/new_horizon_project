from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe


import sys
from datetime import datetime

from apps.account_page.models import Profile
from apps.test_progress.models import AccountTestProgress

from misc.template_styling_components import show_test_card


# @register_user_activity
@login_required()
def view_account_page(request):

    res = []

    user_profile = Profile.objects.get(user_id=request.user.pk)

    for test_progress in AccountTestProgress.objects.filter(profile=user_profile.pk):

        res.append(
            show_test_card(
                test=test_progress.tests.first(),
                test_progress=test_progress,
            )
        )

    context = {
        "tests_list": mark_safe('<div class="test_row">' + "".join(res) + "</div>"),
        "user": request.user,
        "profile": user_profile,
    }

    return render(request, "account_page.html", context)
