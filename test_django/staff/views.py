from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView, TemplateView, ListView

from .forms import AuthForm, GuestForm, PaymentForm, RoomForm, QuestionFormStaff
from .models import Guest, Payment, Room
from lending.models import Booking, Question
from lending.forms import BookingForm


"""Представление отображения главной страницы"""


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'staff_index.html'


"""Представления отображения записей БД"""


class Rooms(LoginRequiredMixin, ListView):
    template_name = 'data/staff_rooms.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = self.get_queryset()
        return context

    def get_queryset(self):
        return Room.objects.all().order_by('room')


class Guests(LoginRequiredMixin, ListView):
    template_name = 'data/staff_guests.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['guests'] = self.get_queryset()
        return context

    def get_queryset(self):
        return Guest.objects.all().order_by('full_name')


class Bookings(LoginRequiredMixin, ListView):
    template_name = 'data/staff_bookings.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = self.get_queryset()
        return context

    def get_queryset(self):
        return Booking.objects.all()


class Payments(LoginRequiredMixin, ListView):
    template_name = 'data/staff_payments.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payments'] = self.get_queryset()
        return context

    def get_queryset(self):
        return Payment.objects.all().order_by('date')


class Questions(LoginRequiredMixin, ListView):
    template_name = 'data/staff_questions.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = self.get_queryset()
        return context

    def get_queryset(self):
        return Question.objects.filter(status='Не отвечено')


"""Представления добавления записей в БД"""


class AddBooking(LoginRequiredMixin, View):
    def get(self, request):
        form = BookingForm()
        model_name = 'Брони'
        context = {
            'form': form,
            'model_name': model_name,
        }
        return render(request, template_name='action/add.html', context=context)

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse(
                    {
                        'message': 'Бронь добавлена',
                        'color': 'green',
                    }
                )
            except ValidationError:
                return JsonResponse(
                    {'message': 'Ошибка валидации формы',
                     'color': 'red',
                     })
        else:
            return JsonResponse(
                {'message': 'Некорректный ввод данных',
                 'color': 'red',
                 })


class AddGuest(LoginRequiredMixin, View):
    def get(self, request):
        form = GuestForm()
        model_name = 'Гости'
        context = {
            'form': form,
            'model_name': model_name,
        }
        return render(request, template_name='action/add.html', context=context)

    def post(self, request):
        form = GuestForm(request.POST)
        if form.is_valid():
            room = Room.objects.get(room=form['room'].data)
            if room.availability == 'Занято':
                return JsonResponse({
                    'message': 'Выбранный номер занят',
                    'color': 'red',
                })
            try:
                form.save()
                room.availability = 'Занято'
                room.save()
                return JsonResponse(
                    {
                        'message': 'Успещная регистрация гостя',
                        'color': 'green',
                    }
                )
            except ValidationError:
                return JsonResponse(
                    {'message': 'Ошибка валидации формы',
                     'color': 'red',
                     })
        else:
            return JsonResponse(
                {'message': 'Некорректный ввод данных',
                 'color': 'red',
                 })


class AddRoom(LoginRequiredMixin, View):
    def get(self, request):
        form = RoomForm()
        model_name = 'Номера'
        context = {
            'form': form,
            'model_name': model_name,
        }
        return render(request, template_name='action/add.html', context=context)

    def post(self, request):
        form = RoomForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse(
                    {
                        'message': 'Успешный платеж',
                        'color': 'green',
                    }
                )
            except ValidationError:
                return JsonResponse(
                    {'message': 'Ошибка валидации формы',
                     'color': 'red',
                     })
        else:
            return JsonResponse(
                {'message': 'Некорректный ввод данных',
                 'color': 'red',
                 })


class AddPayment(LoginRequiredMixin, View):
    def get(self, request):
        form = PaymentForm()
        model_name = 'Платежи'
        context = {
            'form': form,
            'model_name': model_name,
        }
        return render(request, template_name='action/add.html', context=context)

    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse(
                    {
                        'message': 'Успешный платеж',
                        'color': 'green',
                    }
                )
            except ValidationError:
                return JsonResponse(
                    {'message': 'Ошибка валидации формы',
                     'color': 'red',
                     })
        else:
            return JsonResponse(
                {'message': 'Некорректный ввод данных',
                 'color': 'red',
                 })


"""Представления изменения записей в БД"""


class ChangeBooking(LoginRequiredMixin, View):
    def get(self, request, pk):
        booking_obj = get_object_or_404(Booking, id=pk)
        form = BookingForm({
            'full_name': booking_obj.full_name,
            'phone': booking_obj.phone,
            'date_in': booking_obj.date_in,
            'date_out': booking_obj.date_out,
            'room': booking_obj.room,
            'requests': booking_obj.requests,
        })
        model_name = 'Брони'
        template_name = 'action/update.html'
        context = {
            'form': form,
            'model_name': model_name,
        }
        return render(request, template_name=template_name, context=context)

    def post(self, request, pk):
        booking_obj = get_object_or_404(Booking, id=pk)
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                booking_obj.full_name = data['full_name']
                booking_obj.phone = data['phone']
                booking_obj.date_in = data['date_in']
                booking_obj.date_out = data['date_out']
                booking_obj.room = data['room']
                booking_obj.requests = data['requests']
                booking_obj.save()
                return JsonResponse(
                    {
                        'message': 'Данные о брони изменены',
                        'color': 'green',
                    }
                )
            except ValidationError:
                return JsonResponse(
                    {'message': 'Ошибка валидации формы',
                     'color': 'red',
                     })
        else:
            return JsonResponse(
                {'message': 'Некорректный ввод данных',
                 'color': 'red',
                 })


class ChangeGuest(LoginRequiredMixin, View):
    def get(self, request, pk):
        guest_obj = get_object_or_404(Guest, id=pk)
        form = GuestForm({
            'full_name': guest_obj.full_name,
            'phone': guest_obj.phone,
            'date_in': guest_obj.date_in,
            'date_out': guest_obj.date_out,
            'email': guest_obj.email,
            'birth': guest_obj.birth,
            'passport': guest_obj.passport,
            'room': guest_obj.room,
        })
        model_name = 'Гости'
        template_name = 'action/update.html'
        context = {
            'form': form,
            'model_name': model_name,
        }
        return render(request, template_name=template_name, context=context)

    def post(self, request, pk):
        guest_obj = get_object_or_404(Guest, id=pk)
        form = GuestForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                if data['room'].availability == 'Занято':
                    return JsonResponse(
                        {'message': 'Этот номер уже занят',
                         'color': 'red',
                         })
                if guest_obj.room != data['room']:
                    guest_obj.room.availability = 'Свободно'
                    data['room'].availability = 'Занято'
                    guest_obj.room.save()
                    data['room'].save()
                guest_obj.full_name = data['full_name']
                guest_obj.phone = data['phone']
                guest_obj.date_in = data['date_in']
                guest_obj.date_out = data['date_out']
                guest_obj.email = data['email']
                guest_obj.birth = data['birth']
                guest_obj.passport = data['passport']
                guest_obj.room = data['room']
                guest_obj.save()
                return JsonResponse(
                    {
                        'message': 'Данные о госте изменены',
                        'color': 'green',
                    }
                )
            except ValidationError:
                return JsonResponse(
                    {'message': 'Ошибка валидации формы',
                     'color': 'red',
                     })
        else:
            return JsonResponse(
                {'message': 'Некорректный ввод данных',
                 'color': 'red',
                 })


class ChangeRoom(LoginRequiredMixin, View):
    def get(self, request, pk):
        room_obj = get_object_or_404(Room, id=pk)
        form = RoomForm({
            'room': room_obj.room,
            'category': room_obj.category,
            'availability': room_obj.availability,
        })
        model_name = 'Номера'
        template_name = 'action/update.html'
        context = {
            'form': form,
            'model_name': model_name,
        }
        return render(request, template_name=template_name, context=context)

    def post(self, request, pk):
        room_obj = get_object_or_404(Room, id=pk)
        form = RoomForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                room_obj.full_name = data['room']
                room_obj.category = data['category']
                room_obj.availability = data['availability']
                room_obj.save()
                return JsonResponse(
                    {
                        'message': 'Данные о госте изменены',
                        'color': 'green',
                    }
                )
            except ValidationError:
                return JsonResponse(
                    {'message': 'Ошибка валидации формы',
                     'color': 'red',
                     })
        else:
            return JsonResponse(
                {'message': 'Некорректный ввод данных',
                 'color': 'red',
                 })


class ChangePayment(LoginRequiredMixin, UpdateView):
    def get(self, request, pk):
        payment_obj = get_object_or_404(Payment, id=pk)
        form = PaymentForm({
            'guest': payment_obj.guest,
            'payment': payment_obj.payment,
        })
        model_name = 'Платежи'
        template_name = 'action/update.html'
        context = {
            'form': form,
            'model_name': model_name,
        }
        return render(request, template_name=template_name, context=context)

    def post(self, request, pk):
        payment_obj = get_object_or_404(Payment, id=pk)
        form = PaymentForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                payment_obj.guest = data['guest']
                payment_obj.payment = data['payment']
                payment_obj.save()
                return JsonResponse(
                    {
                        'message': 'Данные о госте изменены',
                        'color': 'green',
                    }
                )
            except ValidationError:
                return JsonResponse(
                    {'message': 'Ошибка валидации формы',
                     'color': 'red',
                     })
        else:
            return JsonResponse(
                {'message': 'Некорректный ввод данных',
                 'color': 'red',
                 })


"""Представления удаления записей из БД"""


class DeleteBooking(LoginRequiredMixin, View):
    def get(self, request, pk):
        booking_obj = get_object_or_404(Booking, id=pk)
        booking_obj.delete()
        return redirect('staff:bookings')


class DeleteGuest(LoginRequiredMixin, View):
    def get(self, request, pk):
        guest_obj = get_object_or_404(Guest, id=pk)
        guest_obj.delete()
        return redirect('staff:guests')


class DeleteQuestion(LoginRequiredMixin, View):
    def get(self, request, pk):
        question_obj = get_object_or_404(Question, id=pk)
        question_obj.delete()
        return redirect('staff:questions')


"""Представления обработки специфичных операций"""


class RegisterBooking(LoginRequiredMixin, View):
    def get(self, request, pk):
        booking_to_register = get_object_or_404(Booking, id=pk)
        form = GuestForm({'full_name': booking_to_register.full_name,
                          'phone': booking_to_register.phone,
                          'date_in': booking_to_register.date_in,
                          'date_out': booking_to_register.date_out,
                          'room': booking_to_register.room,
                          }
                         )
        model_name = 'Гости'
        context = {
            'form': form,
            'model_name': model_name
        }
        return render(request, template_name='action/add.html', context=context)

    def post(self, request, pk):
        booking_to_register = get_object_or_404(Booking, id=pk)
        form = GuestForm(request.POST)
        if form.is_valid():
            room = Room.objects.get(room=form['room'].data)
            if room.availability == 'Занято':
                return JsonResponse({
                    'message': 'Выбранный номер занят',
                    'color': 'red',
                })
            try:
                form.save()
                room.availability = 'Занято'
                room.save()
                booking_to_register.delete()
                return JsonResponse(
                    {
                        'message': 'Успешная регистрация брони',
                        'color': 'green',
                    }
                )
            except ValidationError:
                return JsonResponse(
                    {'message': 'Ошибка валидации формы',
                     'color': 'red',
                     })
        else:
            return JsonResponse(
                {'message': 'Некорректный ввод данных',
                 'color': 'red',
                 })


class AnswerQuestion(LoginRequiredMixin, View):
    def get(self, request, pk):
        question_obj = get_object_or_404(Question, id=pk)
        form = QuestionFormStaff({
            'question': question_obj.question,
        })
        name = question_obj.name
        context = {
            'form': form,
            'name': name,
        }
        return render(request, template_name='action/answer_question.html', context=context)

    def post(self, request, pk):
        form = QuestionFormStaff(request.POST)
        if form.is_valid():
            try:
                question_obj = get_object_or_404(Question, id=pk)
                question_obj.answer = form.cleaned_data['answer']
                question_obj.status = 'Отвечено'
                question_obj.save()
                return JsonResponse(
                    {
                        'message': 'Ответ отправлен',
                        'color': 'green',
                    }
                )
            except ValidationError:
                return JsonResponse(
                    {'message': 'Ошибка валидации формы',
                     'color': 'red',
                     })
        else:
            return JsonResponse(
                {'message': 'Некорректный ввод данных',
                 'color': 'red',
                 })


"""Представления авторизации пользователей (login/logout)"""


class LoginUser(LoginView):
    form_class = AuthForm
    template_name = 'auth/staff_auth.html'


class LogoutUser(LoginRequiredMixin, LogoutView):
    pass
