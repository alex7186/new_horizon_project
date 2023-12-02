from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required


@login_required()
def view_account_page(request):

    context = {}

    return render(request, "account_page.html", context)
