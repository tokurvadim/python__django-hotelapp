# Generated by Django 4.2.5 on 2023-12-17 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0010_alter_guest_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='room',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='staff.room'),
        ),
    ]
