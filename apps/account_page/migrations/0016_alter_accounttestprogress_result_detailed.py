# Generated by Django 4.1.5 on 2024-01-07 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account_page", "0015_accounttestprogress_result_detailed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accounttestprogress",
            name="result_detailed",
            field=models.JSONField(default=dict),
        ),
    ]
