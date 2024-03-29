# Generated by Django 4.2.5 on 2024-01-05 09:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0024_alter_booking_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='patronymic',
        ),
        migrations.AddField(
            model_name='booking',
            name='full_name',
            field=models.CharField(default='', max_length=210, validators=[django.core.validators.RegexValidator(regex='\\w+\\s+\\w+\\s+\\w+')]),
        ),
    ]
