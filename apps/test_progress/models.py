from django.db import models
import random

from apps.account_page.models import Profile

from datetime import datetime


class TestObject(models.Model):

    test_object_name = models.CharField(max_length=100, verbose_name="Название")
    test_required_result = models.IntegerField(default=75)
    test_max_result = models.IntegerField(default=50)

    test_type = models.CharField(max_length=100, default="1")

    def __str__(self) -> str:
        return self.test_object_name

    class Meta:
        verbose_name = "3.2. Тест (Выбор вариантов)"
        verbose_name_plural = "3.2. Тесты (Выбор вариантов)"


class Question(models.Model):

    test_object = models.ForeignKey(
        TestObject, related_name="test_object", on_delete=models.CASCADE
    )

    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question

    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question=self))
        data = []
        random.shuffle(answer_objs)

        for answer_obj in answer_objs:
            data.append(
                {"answer": answer_obj.answer, "is_correct": answer_obj.is_correct}
            )
        return data

    class Meta:
        verbose_name = "3.2.1. Вопрос (Выбор вариантов)"
        verbose_name_plural = "3.2.1. Вопросы (Выбор вариантов)"


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name="question_answer", on_delete=models.CASCADE
    )

    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer

    class Meta:
        verbose_name = "3.2.2. Вариант ответа (Выбор вариантов)"
        verbose_name_plural = "3.2.2. Варианты ответа (Выбор вариантов)"


class AccountTestProgress(models.Model):
    profile = models.ManyToManyField(Profile)
    tests = models.ManyToManyField(TestObject)

    current_status = models.IntegerField(default=0)
    # 0 - Не начато
    # 1 - В процессе
    # 2 - Завершено

    # result = models.JSONField(null=True)
    result = models.IntegerField(default=-1)
    result_detailed = models.JSONField(default=dict({"total_points": 0, "answers": {}}))
    # 0.0 - не пройдено или результат 0%
    # 0.0 - 1.0 - результат в процентах для type=1
    # 1.0 - пройдено или результат 100%

    attemp_started = models.DateTimeField(default=datetime(1970, 1, 1))
    attemp_finished = models.DateTimeField(default=datetime(1970, 1, 1))

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        test = self.tests.first()

        if self.result == -1:
            self.current_status = 0
        elif self.result < test.test_required_result:
            self.current_status = 2
        elif self.result >= test.test_required_result:
            self.current_status = 3

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "3.1. Назначение теста"
        verbose_name_plural = "3.1. Назначения теста"
