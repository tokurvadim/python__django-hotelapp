from django.core.validators import RegexValidator
from django.db import models

from staff.models import RoomCategory


class Question(models.Model):
    name = models.CharField(max_length=150, default='')
    email = models.EmailField(default='')
    question = models.TextField(default='')
    answer = models.CharField(default='', blank=True)
    status = models.CharField(max_length=300, default='Не отвечено', choices=[
        ('Отвечено', 'Отвечено'),
        ('Не отвечено', 'Не отвечено')
    ])


class Booking(models.Model):
    CATEGORY_CHOICE = [(obj.category, obj.category) for obj in RoomCategory.objects.all()]

    full_name = models.CharField(max_length=210, default='', validators=[RegexValidator(regex=r'\w+\s+\w+\s+\w+')])
    phone = models.CharField(default='', validators=[RegexValidator(regex=r'(?:\+7|8)\d{10}')])
    date_in = models.DateField()
    date_out = models.DateField()
    room = models.CharField(choices=CATEGORY_CHOICE)
    requests = models.CharField(max_length=50, default='', blank=True)
