from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib import messages


def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'accounts/logout.html')

def register(request):
    form = CreateUserForm()

    if request.method== 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
