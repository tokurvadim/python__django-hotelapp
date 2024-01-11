from django.contrib import admin
from .models import Question, Booking


@admin.register(Question)
class Question(admin.ModelAdmin):
    pass


@admin.register(Booking)
class Booking(admin.ModelAdmin):
    pass
