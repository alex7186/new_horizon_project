# Generated by Django 4.1.4 on 2023-12-02 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account_page", "0005_remove_accounttestprogress_profile_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"verbose_name_plural": "Профиль"},
        ),
    ]
