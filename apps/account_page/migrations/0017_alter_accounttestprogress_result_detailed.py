# Generated by Django 4.1.5 on 2024-01-07 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account_page", "0016_alter_accounttestprogress_result_detailed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accounttestprogress",
            name="result_detailed",
            field=models.JSONField(default={"answers": {}, "total_points": 0}),
        ),
    ]
