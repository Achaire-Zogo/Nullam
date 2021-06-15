from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from .models import Event, Ticket, Cathegorie, Order, OrderEvent, ShippinrAddress,AchatTicket,Publish
from .forms import EventAddForm, TicketAddForm,AchatTicketForm
from django.utils.text import slugify
from django.http import JsonResponse
import json

from django.contrib.auth.decorators import login_required


# function to add movie from the html forms
@login_required(login_url='login')
def add_Event(request):
    if request.method == 'POST':
        form = EventAddForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
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
    eve = Publish.objects.get(id=id)  # select * from event where id=id

    context = {
        "eve": eve
    }
    return render(request, 'events/details.html', context)
    



def home(request):
    allevents = Publish.objects.all()

    context = {
        "allevents": allevents
    }

    return render(request, 'events/index.html', context)


def about(request):
    return render(request, 'events/about.html')


@login_required(login_url='login')
def add_Event(request):
    if request.method == 'POST':
        form = EventAddForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.promotor = request.user.promotor
            event.slug = slugify(event.name)
            event.save()

            return redirect('dashboard')
    else:
        form = EventAddForm()

    return render(request, 'events/create-event.html', {'form': form})

    
def payment_step(request,id=None):
    
    em = request.POST.get("test")
    tel = request.POST.get("test1")
    tqt = request.POST.get("test2")
    tta = request.POST.get("test3")
    ticket_infos = AchatTicket(Email_customer=em,Phone_number=tel,Ticket_quantity=tqt,Total_amount=tta)
        

    ticket_infos.save()
    pk = ticket_infos.id
    qt = ticket_infos.Ticket_quantity
    qr = ticket_infos.qr_code
    total = ticket_infos.Total_amount
    price = int(total)/int(qt)   
        
        
    context={ 
        "pk": pk,
        "price": price,
        "qt": qt,
        "qr": qr,
        "total": total
    }
        
  

    print("hello submited")
    

    return render(request, 'events/facture.html', context)





@login_required(login_url='login')
def paiment(request, id,transaction_id=None):

    if request.user.is_authenticated:
        promotor = request.user.promotor
        itms =Publish.objects.get(id=id)
    
    if request.method == 'POST':
        tik = Ticket.objects.get(id=id)
        form = AchatTicketForm(request.POST)
        if form.is_valid():
            orde = form.save(commit=False)
            orde.Event_promotor = request.user.promotor
            orde.Event_ticket = tik
            
            orde.save()

            vl = tik.id
            e = 93
            
            
            return redirect('/checkout/'+str(vl)+'/'+str(e))
    else:
        form = AchatTicketForm()
    context = {
        "itms": itms,
        "form": form
    }

    return render(request, 'events/paiment.html', context)



@login_required(login_url='login')

def checkout(request):
   
   
    return render(request, 'events/checkout.html')


def payment(request, id):
    return render(request, 'events/facture.html')




def facture(request):
    vnm = AchatTicket.objects.all()
    context = {
        "vnm" : vnm
    }
    return render(request, 'events/facture.html', context)


def recieve(request, id):

    idr = AchatTicket.objects.get(id=id) 
    ids =idr.id  
    print(ids) 

    rvce = AchatTicket.objects.get(id=id)
    context = {
        "rvce":rvce
    }
    return render(request, 'events/facture.html', context)