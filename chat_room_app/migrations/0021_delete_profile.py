# Generated by Django 5.1.4 on 2025-01-29 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_room_app', '0020_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
