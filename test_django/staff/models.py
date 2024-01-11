from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, EmailValidator


class RoomCategory(models.Model):
    category = models.CharField(max_length=50, default='', unique=True)
    price = models.IntegerField(default=0, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.category


class Room(models.Model):
    AVAILABILITY_CHOICES = [
        ('Занято', 'Занято'),
        ('Свободно', 'Свободно'),
    ]

    room = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(9999)], unique=True)
    category = models.ForeignKey('RoomCategory', on_delete=models.PROTECT, default=1)
    availability = models.CharField(choices=AVAILABILITY_CHOICES, default='Свободно',)

    def __str__(self):
        return str(self.room)


class Guest(models.Model):
    full_name = models.CharField(max_length=150, default='', validators=[RegexValidator(regex=r'\w+\s{1}\w+\s{1}\w*',)])
    phone = models.CharField(validators=[RegexValidator(regex=r'(?:\+7|8)\d{10}')], null=True)
    date_in = models.DateField(null=True)
    date_out = models.DateField(null=True)
    email = models.EmailField(validators=[EmailValidator], null=True, default='')
    birth = models.DateField(null=True)
    passport = models.SlugField(validators=[RegexValidator(regex=r'\d{4}-\d{6}',)], default='0000-000000')
    room = models.ForeignKey('Room', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.full_name


class Payment(models.Model):
    guest = models.ForeignKey('Guest', on_delete=models.SET_DEFAULT, default='')
    payment = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    date = models.DateField(auto_now_add=True, null=True)
