# Generated by Django 4.1.4 on 2024-02-24 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account_page", "0023_profile_is_admin"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AccountTestProgress",
        ),
    ]
