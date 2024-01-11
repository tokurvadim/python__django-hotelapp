from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, View

from .forms import QuestionformLending, BookingForm


class Index(View):
    def get(self, request):
        template_name = 'lending_index.html'
        form = QuestionformLending()
        context = {
            'form': form,
        }
        return render(request, template_name=template_name, context=context)

    def post(self, request):
        form = QuestionformLending(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse(
                    {'message': 'Ваш вопрос отправлен администратору. Спасибо!',
                     'color': 'green',
                     })
            except ValidationError as e:
                return JsonResponse(
                    {'message': f'{e.message}',
                     'color': 'red',
                     })
        else:
            return JsonResponse(
                {'message': 'Некорректные данные формы',
                 'color': 'red',
                 })


class Rooms(TemplateView):
    template_name = 'lending_rooms.html'


class Booking(View):
    def get(self, request):
        template_name = 'lending_booking.html'
        form = BookingForm
        context = {
            'form': form,
        }
        return render(request, template_name=template_name, context=context)

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse(
                    {'message': 'Спасибо за выбор нашей гостиницы! Ждем Вас в указанное в брони время!',
                     'color': 'green',
                     })
            except ValidationError as e:
                return JsonResponse(
                    {'message': f'{e.message}',
                     'color': 'red',
                     })
        else:
            return JsonResponse(
                {'message': 'Некорректное заполнение данных',
                 'color': 'red',
                 })


class Contacts(TemplateView):
    template_name = 'lending_contacts.html'
