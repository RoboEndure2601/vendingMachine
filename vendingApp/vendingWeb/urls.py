from django.contrib import admin
from django.urls import path
from vendingWeb import views

urlpatterns = [
    path("", views.index, name='home'),
]