# Generated by Django 4.1.4 on 2023-12-17 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0006_alter_article_options_alter_category_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={
                "verbose_name": "2.1. Статья",
                "verbose_name_plural": "2.1. Статьи",
            },
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "verbose_name": "2.2. Категория",
                "verbose_name_plural": "2.2. Категории",
            },
        ),
    ]