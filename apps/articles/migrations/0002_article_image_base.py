# Generated by Django 4.1.4 on 2023-11-19 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="image_base",
            field=models.ImageField(
                default="static/img/solid-color-image.png", upload_to="static/img"
            ),
        ),
    ]