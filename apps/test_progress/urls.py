from django.urls import path

from apps.test_progress.views import (
    test_description,
    question_details,
)


urlpatterns = [
    # тесты
    path("tests/<int:pk>/", test_description, name="test_description"),
    # вопросы
    path("tests/<int:pk>/<int:question_pk>", question_details, name="question_details"),
]
