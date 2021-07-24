from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.event_home, name='event_home'),
    path('about', views.about, name='about'),
    # path('event_home', views.event_home, name='event_home'),
    path('event_detail/<int:id>', views.event_detail, name='event_detail'),
    path('event_shipping/<int:id>', views.event_shipping, name='event_shipping'),
    path('event_facture', views.event_facture, name='event_facture'),
    path('event_confirmation_pay/<int:id>', views.event_confirmation_pay, name='event_confirmation_pay'), 
    path('facture/', views.facture, name='facture'),
    path('pdf', views.pdf, name='pdf'),
    path('pdfnew/<pk>', views.pdfnew, name='pdfnew'),
    path('pdfview/<pk>', views.pdfview, name='pdfview'),
    path('recieve/<int:id>', views.recieve, name='recieve'),

]
