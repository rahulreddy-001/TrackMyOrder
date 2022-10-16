from django.contrib import admin
from django.urls import path
import website.views as views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('register_user', views.register_user, name='register_user'),
    path('login', views.login, name='login'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('generate_order', views.generate_order, name='generate_order'),
    path('transport', views.transport, name='transport'),
    path('transport_order', views.transport_order, name='transport_order'),
    path('warehouse', views.warehouse, name='warehouse'),
    path('warehouse_log', views.warehouse_log, name='warehouse_log'),
    path('delivery', views.delivery, name='delivery'),
    path('out_delivery', views.out_delivery, name='out_delivery'),
    path('track', views.track, name='track'),
    path('track_order', views.track_order, name='track_order'),
]
