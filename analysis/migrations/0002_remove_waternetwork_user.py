# Generated by Django 5.1.7 on 2025-06-13 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("analysis", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="waternetwork",
            name="user",
        ),
    ]
