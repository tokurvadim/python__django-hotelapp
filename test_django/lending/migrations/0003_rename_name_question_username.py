# Generated by Django 4.2.5 on 2023-12-03 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0002_rename_questions_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='name',
            new_name='username',
        ),
    ]
