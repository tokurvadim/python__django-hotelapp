# Generated by Django 4.2.5 on 2024-01-01 20:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0011_alter_guest_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='full_name',
            field=models.CharField(default='', max_length=150, validators=[django.core.validators.RegexValidator(regex='\\w+\\s{1}\\w+\\s{1}\\w*')]),
        ),
        migrations.AlterField(
            model_name='guest',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='staff.room'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('guest', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='staff.guest')),
            ],
        ),
    ]