# Generated by Django 4.2.5 on 2024-01-02 13:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0018_alter_booking_first_name_alter_booking_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='first_name',
            field=models.CharField(default='', max_length=70, validators=[django.core.validators.RegexValidator(regex='(?:а-яА-Я)+')]),
        ),
    ]
