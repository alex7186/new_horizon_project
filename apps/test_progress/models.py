from django.db import models
import random


class TestObject(models.Model):

    test_object_name = models.CharField(max_length=100)
    test_required_result = models.IntegerField(default=75)
    test_max_result = models.IntegerField(default=50)

    test_type = models.CharField(max_length=100, default="1")

    def __str__(self) -> str:
        return self.test_object_name

    class Meta:
        verbose_name = "3.1. Тест (Выбор вариантов)"
        verbose_name_plural = "3.1. Тесты (Выбор вариантов)"


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
        verbose_name = "3.2. Вариант ответа (Выбор вариантов)"
        verbose_name_plural = "3.2. Вариант ответа (Выбор вариантов)"


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name="question_answer", on_delete=models.CASCADE
    )

    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer
