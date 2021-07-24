from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from events.models import Ticket

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']


class TicketAddForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('maximum_attende',
        'price',
        'ticket_cathegories',
        'ticket_start_date_sell',
        'ticket_start_time_sell',
        'ticket_end_date_sell',
        'ticket_end_time_sell',
        'min_ticket',
        'max_ticket',)
        widgets = {
            'ticket_start_date_sell': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ticket_end_date_sell': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ticket_start_time_sell': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'ticket_end_time_sell': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
        }