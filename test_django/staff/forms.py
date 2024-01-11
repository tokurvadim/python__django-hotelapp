from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Room, Guest, Payment, RoomCategory
from lending.models import Question


class AuthForm(AuthenticationForm):
    username = forms.CharField(required=True, label="Имя пользователя:", widget=forms.TextInput(attrs={
        'class': 'form_input',
        'id': 'input_username',
        'placeholder': 'Логин',
    }))
    password = forms.CharField(required=True, label="Пароль:", widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form_input',
        'id': 'input_password',
        'placeholder': 'Логин',
    }))


class GuestForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=Room.objects.all().order_by('category'), empty_label='', label='Номер:', widget=forms.Select(attrs={
        'class': 'monserrat_light form_input',
        'id': 'input_room',
    }))

    class Meta:
        model = Guest
        fields = '__all__'
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
            'email': forms.EmailInput(attrs={
                'type': 'email',
                'class': 'monserrat_light form_input',
                'id': 'input_email',
            }),
            'birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'monserrat_light form_input',
                'id': 'input_birth',
            }),
            'passport': forms.TextInput(attrs={
                'placeholder': '0000-000000',
                'class': 'monserrat_light form_input',
                'id': 'input_passport',
            }),
        }
        labels = {
            'full_name': 'ФИО:',
            'phone': 'Ваш телефон:',
            'date_in': 'Дата въезда:',
            'date_out': 'Дата выезда:',
            'email': 'Email:',
            'birth': 'День рождения:',
            'passport': 'Паспорт:',
            'room': 'Номер',
        }


class PaymentForm(forms.ModelForm):
    guest = forms.ModelChoiceField(queryset=Guest.objects.all(), empty_label='', label='Гость:', widget=forms.Select(attrs={
        'class': 'monserrat_light form_input',
        'id': 'input_fullname',
    }))

    class Meta:
        model = Payment
        fields = ['guest', 'payment']
        widgets = {
            'payment': forms.NumberInput(attrs={
                'type': 'tel',
                'class': 'monserrat_light form_input',
                'id': 'input_payment',
            })
        }
        labels = {
            'payment': 'Платёж:'
        }


class RoomForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=RoomCategory.objects.all(), empty_label='', label='Категория:', widget=forms.Select(attrs={
        'class': 'monserrat_light form_input',
        'id': 'input_category',
    }))

    class Meta:
        model = Room
        fields = ['room', 'category']
        widgets = {
            'room': forms.NumberInput(attrs={
                'type': 'tel',
                'class': 'monserrat_light form_input',
                'id': 'input_room',
            }),
        }
        labels = {
            'room': 'Номер:',
        }


class QuestionFormStaff(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question', 'answer']
        widgets = {
            'question': forms.TextInput(attrs={
                'readonly': True,
                'class': 'monserrat_light form_input',
                'id': 'input_question',
            }),
            'answer': forms.Textarea(attrs={
                'required': True,
                'minlength': 20,
                'class': 'monserrat_light form_input',
                'id': 'input_answer',
            }),
        }
        labels = {
            'question': 'Вопрос:',
            'answer': 'Ответ:'
        }
