# Generated by Django 4.2.5 on 2023-12-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending', '0005_alter_question_question_alter_question_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('datein', models.DateField()),
                ('dateout', models.DateField()),
                ('room', models.CharField(max_length=50)),
                ('requests', models.CharField(default='NULL', max_length=50)),
            ],
        ),
    ]
