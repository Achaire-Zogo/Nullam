from django.shortcuts import render, redirect

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'accounts/logout.html')

def register(request):
    return render('register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
