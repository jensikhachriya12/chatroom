# Generated by Django 5.1.4 on 2025-01-22 16:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_room_app', '0007_alter_customers_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='mobile_no',
            field=models.BigIntegerField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Mobile number must be exactly 10 digits.', regex='^\\d{10}$')]),
        ),
    ]
