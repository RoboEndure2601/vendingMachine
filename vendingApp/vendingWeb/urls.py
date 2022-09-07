from django.urls import path
from vendingWeb import views
from . import views

urlpatterns = [
    path("", views.index, name='home')
]