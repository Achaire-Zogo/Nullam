from django.shortcuts import render

def index(request):
    return render(request, 'nullam/index.html')

def about(request):
    return render(request, 'nullam/about.html')