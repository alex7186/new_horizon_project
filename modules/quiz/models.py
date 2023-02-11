from django.db import models
from django_mysql.models import ListTextField


# Create your models here.
class QuizPick4(models.Model):
    question_title = models.CharField(max_length=200, null=True)
    question_main_text = models.TextField(
        default="Основной текст опроса (содержит сам вопрос)"
    )

    options = ListTextField(
        base_field=models.CharField(max_length=200, default=""),
        size=10,
        default=None,
    )

    answer = models.IntegerField(default=1)

    error_explanation = models.TextField(
        default="Текст с утешением и объяснением, какой вариант правильный"
    )
    success_congratulations = models.TextField(
        default="Текст с поздравлением об успешном прохождении теста"
    )

    def __str__(self):
        return self.question_title
