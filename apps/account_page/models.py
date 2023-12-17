from django.db import models

from django.contrib.auth.models import User
from apps.test_progress.models import TestObject


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self) -> str:
        return self.user.email


class AccountTestProgress(models.Model):
    profile = models.ManyToManyField(Profile)
    tests = models.ManyToManyField(TestObject)

    current_status = models.IntegerField(default=0)
    # 0 - Не начато
    # 1 - В процессе
    # 2 - Завершено

    result = models.JSONField(null=True)
    # 0.0 - не пройдено или результат 0%
    # 0.0 - 1.0 - результат в процентах для type=1
    # 1.0 - пройдено или результат 100%

    class Meta:
        verbose_name = "Связка 'Профиль' - 'Тест'"
        verbose_name_plural = "Связки 'Профиль' - 'Тест'"
