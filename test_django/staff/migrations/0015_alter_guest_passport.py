# Generated by Django 4.2.5 on 2024-01-05 10:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0014_alter_payment_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='passport',
            field=models.SlugField(default='0000-000000', validators=[django.core.validators.RegexValidator(regex='\\d{4}-\\d{6}')]),
        ),
    ]