# Generated by Django 4.1.4 on 2024-02-24 20:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account_page", "0027_interfaceuserslist_stored_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="interfaceuserslist",
            name="last_used_at",
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0)),
        ),
    ]
