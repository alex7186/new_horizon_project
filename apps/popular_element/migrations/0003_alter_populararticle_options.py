# Generated by Django 4.1.4 on 2023-12-02 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("popular_element", "0002_alter_populararticle_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="populararticle",
            options={
                "verbose_name": "Элемет 'Популярные статьи'",
                "verbose_name_plural": "Элеметы 'Популярные статьи'",
            },
        ),
    ]