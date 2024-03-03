from datetime import datetime
from django.db import models
import pandas as pd

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = "1.1. Профиль"
        verbose_name_plural = "1.1. Профили"

    def __str__(self) -> str:
        return self.user.email


class InterfaceUsersList(models.Model):

    last_used_at = models.DateTimeField(default=datetime(1970, 1, 1))

    def save(self, *args, **kwargs):
        self.last_used_at = datetime.now()
        super().save(*args, **kwargs)


class InterfaceDownloadUsersList(InterfaceUsersList):

    stored_file = models.FileField(upload_to="", default="files/users.xlsx")

    class Meta:
        verbose_name = "1.5. Выгрузка пользователей (Excel)"
        verbose_name_plural = "1.5. Выгрузка пользователей (Excel)"


class InterfaceUploadUsersList(InterfaceUsersList):

    stored_file = models.FileField(upload_to="", null=True)

    def save(self, *args, **kwargs):

        df = pd.read_excel(self.stored_file)
        # print(df, file=sys.stdout)

        for i in range(len(df)):

            founded_user = User.objects.filter(username=df.iloc[i, 0]).first()

            if founded_user:
                if founded_user.is_superuser or founded_user.is_staff:
                    continue

                else:
                    founded_user.email = df.iloc[i, 0]
                    founded_user.first_name = df.iloc[i, 1]
                    founded_user.last_name = df.iloc[i, 2]
                    founded_user.password = df.iloc[i, 3]

                    founded_user.save()

            else:
                created_user = User.objects.create(
                    username=df.iloc[i, 0],
                    email=df.iloc[i, 0],
                    first_name=df.iloc[i, 1],
                    last_name=df.iloc[i, 2],
                    password=df.iloc[i, 3],
                )

                #
                Profile.objects.create(
                    user=created_user,
                    is_admin=False,
                )
        self.last_used_at = datetime.now()

        # self.save()

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "1.6. Добавление пользователей (Excel)"
        verbose_name_plural = "1.6. Добавление пользователей (Excel)"
