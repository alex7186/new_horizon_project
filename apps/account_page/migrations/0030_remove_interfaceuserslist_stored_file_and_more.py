# Generated by Django 4.1.4 on 2024-03-03 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account_page", "0029_remove_interfaceuserslist_last_used_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="interfaceuserslist",
            name="stored_file",
        ),
        migrations.AddField(
            model_name="interfacedownloaduserslist",
            name="stored_file",
            field=models.FileField(
                default="files/users.xlsx", upload_to="static/files"
            ),
        ),
        migrations.AddField(
            model_name="interfaceuploaduserslist",
            name="stored_file",
            field=models.FileField(null=True, upload_to="static/files"),
        ),
    ]
