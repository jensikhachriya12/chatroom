# Generated by Django 5.1.4 on 2025-01-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_room_app', '0002_chatroom_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='created_by',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
