from django.contrib import admin
from django.urls import path, include
from . import views


app_name="currency_stat"

urlpatterns = [
    path('<str:base>-<str:target>', views.specific_rate, name='specific_rate'),
    path('', views.index, name='index-stats'),    

]
