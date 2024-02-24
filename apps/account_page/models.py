from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = "1.1. Профиль"
        verbose_name_plural = "1.1. Профили"

    def __str__(self) -> str:
        return self.user.email
