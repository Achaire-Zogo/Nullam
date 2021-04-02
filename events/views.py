from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from .models import Event

from django.contrib.auth.decorators import login_required

def details(request, id):
     eve = Event.objects.get(id=id)#select * from event where id=id

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

