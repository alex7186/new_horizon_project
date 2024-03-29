# Generated by Django 4.1.4 on 2024-02-24 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("account_page", "0025_alter_profile_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="InterfaceUsersList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_used_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="InterfaceDownloadUsersList",
            fields=[
                (
                    "interfaceuserslist_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="account_page.interfaceuserslist",
                    ),
                ),
            ],
            options={
                "verbose_name": "1.5. Выгрузка пользователей (Excel)",
                "verbose_name_plural": "1.5. Выгрузка пользователей (Excel)",
            },
            bases=("account_page.interfaceuserslist",),
        ),
        migrations.CreateModel(
            name="InterfaceUploadUsersList",
            fields=[
                (
                    "interfaceuserslist_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="account_page.interfaceuserslist",
                    ),
                ),
            ],
            options={
                "verbose_name": "1.6. Добавление пользователей (Excel)",
                "verbose_name_plural": "1.6. Добавление пользователей (Excel)",
            },
            bases=("account_page.interfaceuserslist",),
        ),
    ]
