from django.db import models

# from django.contrib.auth.models import User
# from apps.account_page.models import Profile


class Test(models.Model):
    header_text = models.TextField(max_length=255)
    detailed_text = models.TextField(max_length=255)

    type = models.IntegerField(default=1)
    # 1 - Процентный результат
    # 2 - Пройдено / Не пройдено

    class Meta:
        verbose_name = "Тест (результаты)"
        verbose_name_plural = "Тесты (результаты)"
