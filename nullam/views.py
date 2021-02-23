from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from .models import Event


def index(request):
    event = Event.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(event, 6)
    try:
        event = paginator.page(page)
    except PageNotAnInteger:
        event = paginator.page(1)
    except EmptyPage:
        event = paginator.page(paginator.num_pages)
    return render(request, 'nullam/index.html', {'event':event})



def about(request):
    return render(request, 'nullam/about.html')
