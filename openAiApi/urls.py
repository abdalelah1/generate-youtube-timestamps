from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
    path("",generate_timestamps,name="generate_timestamps"),
    path("login/",Login,name="Login"),
    path('Logout/',Logout,name='Logout')

 
]