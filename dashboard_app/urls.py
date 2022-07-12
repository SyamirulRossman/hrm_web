from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log_in', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('rent_view', views.rent_view, name='rent_view'),
]