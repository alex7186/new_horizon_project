# Generated by Django 4.1.4 on 2023-11-19 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_article_image_base"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="image_base",
            field=models.ImageField(
                default="img/solid-color-image.png", upload_to="img"
            ),
        ),
    ]
