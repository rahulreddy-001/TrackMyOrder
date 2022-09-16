from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register',views.register,name='register'),
    path('register_user',views.register_user,name='register_user'),
    path('login',views.login,name='login'),
    path('login_user',views.login_user,name='login_user'),
]
