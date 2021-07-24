from django.urls import path

from . import views

urlpatterns = [
    path('login', views.loginpa, name='login'),
    path('home', views.home, name='home'),
    path('manage_event', views.manage_event, name='manage_event'),
    path('add_event', views.add_event, name='add_event'),
    path('add_new_ticket', views.add_new_ticket, name='add_new_ticket'),
    path('publish', views.publish, name='publish'),
    path('onsale', views.onsale, name='onsale'),
    path('details_of_event/(?P<slug>[.\-\w]+)/$', views.details_of_event, name='details_of_event'),
    path('logout', views.logoutuser, name='logout'),
    path('register', views.register, name='register'),

]

