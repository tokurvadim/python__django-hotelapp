from django import forms
from django.core.exceptions import ValidationError

from staff.models import RoomCategory
from .models import Question, Booking


class QuestionformLending(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'email', 'question']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите имя',
                'class': 'monserrat_light input_contact_us',
                'id': 'input_name',
                'required': True}),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Введите email',
                'class': 'monserrat_light input_contact_us',
                'id': 'input_email',
                'required': True}),
            'question': forms.Textarea(attrs={
                'placeholder': 'Введите вопрос',
                'class': 'monserrat_light input_contact_us',
                'id': 'input_question',
                'required': True
            })
        }
        labels = {
            'name': '',
            'email': '',
            'question': ''
        }

    def save(self, commit=True):
        data = self.cleaned_data
        question, created = Question.objects.get_or_create(name=data['name'],
                                                           email=data['email'],
                                                           question=data['question'])
        if created:
            question.save()
        else:
            raise ValidationError(message='Вы уже отправили вопрос')


class BookingForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=RoomCategory.objects.all().order_by('category'), empty_label='', label='Выберите категорию:',
                                  widget=forms.Select(attrs={
                                      'class': 'monserrat_light form_input',
                                      'id': 'input_room',
                                  }))

    class Meta:
        model = Booking
        fields = ['full_name', 'phone', 'date_in', 'date_out', 'room', 'requests']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'monserrat_light form_input',
                'id': 'input_fullname',
            }),
            'phone': forms.NumberInput(attrs={
                'placeholder': '89996665544',
                'type': 'tel',
                'class': 'monserrat_light form_input',
                'id': 'input_phone',
            }),
            'date_in': forms.DateInput(attrs={
                'type': 'date',
                'class': 'monserrat_light form_input',
                'id': 'input_datein',
            }),
            'date_out': forms.DateInput(attrs={
                'type': 'date',
                'class': 'monserrat_light form_input',
                'id': 'input_dateout',
            }),
            'requests': forms.TextInput(attrs={
                'placeholder': 'Важи пожелания',
                'class': 'monserrat_light form_input',
                'id': 'input_requests',
            })
        }
        labels = {
            'full_name': 'ФИО:',
            'phone': 'Ваш телефон:',
            'date_in': 'Дата въезда:',
            'date_out': 'Дата выезда:',
            'requests': 'Доп. пожелания:',
        }



    def validate_date(self, data):
        if data['date_out'] < data['date_in']:
            raise ValidationError(message="Некорректное заполнение данных")
        return True
