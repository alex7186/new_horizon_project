# Generated by Django 4.1.4 on 2023-12-16 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_progress", "0009_testobject_question_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestAnswer",
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
            ],
        ),
        migrations.AlterModelOptions(
            name="testobject",
            options={
                "verbose_name": "Тест (Выбор вариантов)",
                "verbose_name_plural": "Тесты (Выбор вариантов)",
            },
        ),
        migrations.RenameField(
            model_name="question",
            old_name="category",
            new_name="test_object",
        ),
    ]
