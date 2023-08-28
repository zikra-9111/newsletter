from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path( "about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact')
]