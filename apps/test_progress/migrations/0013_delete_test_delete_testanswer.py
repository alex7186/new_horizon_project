# Generated by Django 4.1.4 on 2023-12-17 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("test_progress", "0012_alter_test_options_remove_test_detailed_text_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Test",
        ),
        migrations.DeleteModel(
            name="TestAnswer",
        ),
    ]
