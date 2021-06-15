from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('create-event', views.add_Event, name='create-event'),
    path('add-ticket/<slug:slug>/', views.add_Ticket, name='add-ticket'),
    path('details/<int:id>/', views.details, name='details'),
    path('paiment/<int:id>/', views.paiment, name='paiment'),
    path('checkout', views.checkout, name='checkout'),
    path('payment_step', views.payment_step, name='payment_step'),
    path('facture/', views.facture, name='facture'),
    path('recieve/<int:id>', views.recieve, name='recieve'),

]
