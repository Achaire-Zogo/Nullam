from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# import db
from .models import Promotor
from events.models import Event, Ticket
from events.views import add_Ticket
from events.forms import TicketAddForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


def loginpa(request):
    if request.user.is_authenticated:
        return redirect('events:home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password =request.POST.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('events:home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)
					
    
    
        

def logoutuser(request):

    logout(request)
    return redirect('events:home')

def register(request):
    if request.user.is_authenticated:
        return redirect('events:home')
    else:
        form = CreateUserForm() 
        if request.method== 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()

                login(request, user)

                promotor = Promotor.objects.create(name=user.username, created_by=user)
                cool = form.cleaned_data.get('username')
                messages.success(request, 'account was created for ' + cool)
                return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)


@login_required(login_url='login')
def my_event(request):
    promotor = request.user.promotor
    eventss = promotor.eventss.all()

    context = {'promotor': promotor, 'eventss': eventss}

    return render(request, 'accounts/my_events.html', context)


@login_required(login_url='login')
def dashboard(request):
    promotor = request.user.promotor
    eventss = promotor.eventss.all()
    eventdash = promotor.eventss.all()[0:5]
    total_event = eventss.count()

    context = {'promotor': promotor, 'eventss': eventss, 'total_event': total_event, 'eventdash': eventdash}

    return render(request, 'accounts/dashboard.html', context)


def mydetails(request, slug):
    event = Event.objects.get(slug=slug)  # select * from event where id=id
    promotor = request.user.promotor

    tickets = Ticket.objects.filter(event=event)

    context = {
        "event": event, 'promotor': promotor, 'tickets': tickets
    }
    return render(request, 'accounts/my_detail_event.html', context)
