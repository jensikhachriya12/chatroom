# Generated by Django 5.1.4 on 2025-01-29 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_room_app', '0015_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='status',
        ),
    ]
