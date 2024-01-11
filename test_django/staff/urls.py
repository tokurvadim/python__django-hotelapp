from django.urls import path

from .views import LogoutUser, Index, Bookings, Guests, Rooms, Payments, Questions, AddBooking, AddGuest, \
    AddPayment, AddRoom, ChangeGuest, DeleteGuest, ChangePayment, ChangeBooking, DeleteBooking, RegisterBooking, \
    AnswerQuestion, DeleteQuestion, LoginUser, ChangeRoom

app_name = 'staff'

urlpatterns = [
    path('', LoginUser.as_view()),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('index/', Index.as_view(), name='index'),
    path('bookings/', Bookings.as_view(), name='bookings'),
    path('guests/', Guests.as_view(), name='guests'),
    path('rooms/', Rooms.as_view(), name='rooms'),
    path('payments/', Payments.as_view(), name='payments'),
    path('questions/', Questions.as_view(), name='questions'),
    path('questions/delete/<int:pk>/', DeleteQuestion.as_view(), name='delete_question'),
    path('questions/answer/<int:pk>/', AnswerQuestion.as_view(), name='answer_question'),
    path('bookings/add/', AddBooking.as_view(), name='add_booking'),
    path('bookings/change/<int:pk>/', ChangeBooking.as_view(), name='change_booking'),
    path('bookings/delete/<int:pk>/', DeleteBooking.as_view(), name='delete_booking'),
    path('bookings/register/<int:pk>/', RegisterBooking.as_view(), name='register_booking'),
    path('guests/add/', AddGuest.as_view(), name='add_guest'),
    path('guests/change/<int:pk>/', ChangeGuest.as_view(), name='change_guest'),
    path('guests/delete/<int:pk>/', DeleteGuest.as_view(), name='delete_guest'),
    path('payments/add/', AddPayment.as_view(), name='add_payment'),
    path('payments/change/<int:pk>/', ChangePayment.as_view(), name='change_payment'),
    path('rooms/add/', AddRoom.as_view(), name='add_room'),
    path('rooms/change/<int:pk>/', ChangeRoom.as_view(), name='change_room'),
]
