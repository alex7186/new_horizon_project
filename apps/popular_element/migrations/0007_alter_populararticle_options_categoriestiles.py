# Generated by Django 4.1.4 on 2024-01-02 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0008_alter_article_options"),
        ("popular_element", "0006_alter_populararticle_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="populararticle",
            options={
                "verbose_name": "5.1. Группа 'Избранные статьи'",
                "verbose_name_plural": "5.1. Группы 'Избранные статьи'",
            },
        ),
        migrations.CreateModel(
            name="CategoriesTiles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default="", max_length=40)),
                (
                    "categories",
                    models.ManyToManyField(
                        related_name="tiles", to="articles.category"
                    ),
                ),
            ],
            options={
                "verbose_name": "5.2. Группа 'Плитки с категориями'",
                "verbose_name_plural": "5.2. Группы 'Плитки с категориями'",
            },
        ),
    ]
