# Generated by Django 4.2.5 on 2023-12-16 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_room_number_room_room_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_category',
            new_name='category',
        ),
    ]
