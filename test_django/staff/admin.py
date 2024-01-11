from django.contrib import admin

from .models import Room, RoomCategory, Guest, Payment


@admin.register(Room)
class Room(admin.ModelAdmin):
    pass


@admin.register(RoomCategory)
class RoomCategory(admin.ModelAdmin):
    pass


@admin.register(Guest)
class Guest(admin.ModelAdmin):
    pass


@admin.register(Payment)
class Payment(admin.ModelAdmin):
    pass
