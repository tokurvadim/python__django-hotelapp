# Generated by Django 4.2.5 on 2023-12-03 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('question', models.CharField()),
            ],
        ),
    ]
