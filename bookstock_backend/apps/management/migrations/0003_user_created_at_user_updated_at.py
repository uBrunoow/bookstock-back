# Generated by Django 4.2.6 on 2024-04-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0002_book_created_at_book_updated_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
