from django.urls import path

from .views import Index, Rooms, Booking, Contacts

app_name = 'lending'

urlpatterns = [
    path('', Index.as_view()),
    path('index/', Index.as_view(), name="index"),
    path('rooms/', Rooms.as_view(), name="rooms"),
    path('booking/', Booking.as_view(), name="booking"),
    path('contacts/', Contacts.as_view(), name="contacts"),
]
