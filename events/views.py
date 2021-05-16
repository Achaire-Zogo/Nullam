from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from .models import Event, Ticket, Cathegorie
from .forms import EventAddForm, TicketAddForm
from django.utils.text import slugify

from django.contrib.auth.decorators import login_required


# function to add movie from the html forms
@login_required(login_url='login')
def add_Event(request):
    if request.method == 'POST':
        form = EventAddForm(request.POST, request.FILES)
        if form.is_valid():
            event =form.save(commit=False)
            event.promotor = request.user.promotor
            event.slug = slugify(event.name)
            event.save()

            return redirect('dashboard')
    else:
        form = EventAddForm()

    return render(request, 'events/create-event.html', {'form': form})


def add_Ticket(request, slug):
    if request.method == 'POST':
        nameev = Event.objects.get(slug=slug)
        form = TicketAddForm(request.POST)
        print(nameev)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.promotor = request.user.promotor
            print(ticket.promotor)
            print('hello word')
            ticket.event = nameev
            ticket.slug = slugify(ticket.ticket_cathegories)
            ticket.save()

            return redirect('dashboard')
    else:
        form = TicketAddForm(request.POST)

    return render(request, 'events/add-ticket.html', {'form': form})


def details(request, id):
     eve = Event.objects.get(id=id) #select * from event where id=id

     context = {
         "eve": eve
     }
     return render(request, 'events/details.html', context)
    



def home(request):
    allevents = Event.objects.all()

    context = {
        "allevents": allevents
    }

    return render(request, 'events/index.html', context)



def about(request):
    return render(request, 'events/about.html')

@login_required(login_url='login')
def createevent(request):
    return render(request, 'events/create-event.html')

# @login_required(login_url='login')
# def add_Eventtt(request):
#     if request.user.is_superuser:
#         if request.method == 'POST':
#             form = EventAddForm(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save()
#                 # after saving the form
#                 return redirect("dashboard")
#         else:
#             form = EventAddForm(request.POST, request.FILES)
#         return render(request, 'events/create-event.html', {'form': form})
#     else:
#         return redirect("events:home")