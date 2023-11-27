from django.contrib import admin
from django.urls import path, include


from apps.account_page.views import view_account_page

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("account_page", view_account_page, name="account_page"),
]
