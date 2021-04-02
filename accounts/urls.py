from django.urls import path

from . import views

urlpatterns = [
    path('login', views.loginpa, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard')
]