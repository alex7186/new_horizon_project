from django.db import models
import random

# from django.contrib.auth.models import User
# from apps.account_page.models import Profile


class Test(models.Model):
    header_text = models.CharField(max_length=255)
    detailed_text = models.TextField(max_length=255)

    type = models.IntegerField(default=1)
    # 1 - Процентный результат
    # 2 - Пройдено / Не пройдено

    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question

    def get_answers(self):
        answer_objs = list(TestAnswer.objects.filter(question=self))
        data = []
        random.shuffle(answer_objs)

        for answer_obj in answer_objs:
            data.append(
                {"answer": answer_obj.answer, "is_correct": answer_obj.is_correct}
            )

        return data

    class Meta:
        verbose_name = "Тест (результаты)"
        verbose_name_plural = "Тесты (результаты)"


class TestAnswer(models.Model):
    pass


class TestObject(models.Model):

    test_object_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.test_object_name

    class Meta:
        verbose_name = "Тест (Выбор вариантов)"
        verbose_name_plural = "Тесты (Выбор вариантов)"


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
        verbose_name = "Вопрос (Выбор вариантов)"
        verbose_name_plural = "Вопросы (Выбор вариантов)"


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name="question_answer", on_delete=models.CASCADE
    )

    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer
