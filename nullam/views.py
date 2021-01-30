from django.shortcuts import render
from .models import Event


def index(request):
    event = Event.objects.all()
    return render(request, 'nullam/index.html', {'event':event})


def about(request):
    return render(request, 'nullam/about.html')
