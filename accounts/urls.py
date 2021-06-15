from django.urls import path

from . import views

urlpatterns = [
    path('login', views.loginpa, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('my/events', views.my_event, name='my/events'),
    path('addpublish', views.addpublish, name='addpublish'),
    # path('my/details/<int:id>/', views.mydetails, name='my/details'),
    path('my/details/(?P<slug>[.\-\w]+)/$', views.mydetails, name='my/details')
]
