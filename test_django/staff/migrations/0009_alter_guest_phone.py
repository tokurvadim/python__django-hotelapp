# Generated by Django 4.2.5 on 2023-12-16 20:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_alter_guest_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.CharField(null=True, validators=[django.core.validators.RegexValidator(regex='(?:\\+7|8)\\d{10}')]),
        ),
    ]
