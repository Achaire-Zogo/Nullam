from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('create-event', views.createevent, name='create-event'),
    path('details/<int:id>/', views.details, name='details'),
]
