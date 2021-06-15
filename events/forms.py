from django import forms
from .models import Event, Ticket,AchatTicket

# creating the forms
class EventAddForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name',
         'tag',
         'category',
         'description',
         'location',
         'event_start_date',
         'event_start_time',
         'event_end_date',
         'event_end_time',
         'images_baniere',
         'images_2',)
        widgets = {
            'event_start_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_end_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_start_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'event_end_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

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

class AchatTicketForm(forms.ModelForm):
    class Meta:
        model = AchatTicket
        fields = (
        'Ticket_quantity',
        )

        widgets = {
            
            'Ticket_quantity': forms.TextInput(attrs={'class': 'form-control', 'type': 'text','id':'quantity', 'style': 'width: 70px;background-color:rgb(255, 255, 255);border:rgb(255, 255, 255)'}),
        }
        