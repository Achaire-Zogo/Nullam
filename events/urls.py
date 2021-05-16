from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('create-event', views.add_Event, name='create-event'),
    path('add-ticket/<slug:slug>/', views.add_Ticket, name='add-ticket'),
    path('details/<int:id>/', views.details, name='details'),
]
