# Generated by Django 4.1.4 on 2024-01-02 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("popular_element", "0005_populararticle_title"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="populararticle",
            options={
                "verbose_name": "Группа статей",
                "verbose_name_plural": "Группа статей",
            },
        ),
    ]
