# Generated by Django 4.1.4 on 2023-12-02 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account_page", "0009_alter_accounttestprogress_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"verbose_name": "Профиль", "verbose_name_plural": "Профили"},
        ),
    ]