# Generated by Django 4.1.5 on 2024-01-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account_page", "0020_alter_accounttestprogress_attemp_finished_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
