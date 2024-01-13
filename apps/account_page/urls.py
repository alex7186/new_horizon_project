from django.contrib import admin
from django.urls import path, include


from apps.account_page.views import (
    view_account_page,
    view_tests_passing,
    test_description,
    question_details,
)

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("account_page", view_account_page, name="account_page"),
    # тесты
    path("tests/<int:pk>/", test_description, name="test_description"),
    # вопросы
    path("tests/<int:pk>/<int:question_pk>", question_details, name="question_details"),
]
