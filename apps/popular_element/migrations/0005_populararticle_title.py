# Generated by Django 4.1.4 on 2024-01-02 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("popular_element", "0004_alter_populararticle_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="populararticle",
            name="title",
            field=models.CharField(default="", max_length=40),
        ),
    ]
