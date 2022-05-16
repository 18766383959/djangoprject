from django.contrib import admin
from django.urls import path, include

from my_app import views

urlpatterns = [
    path('index/',views.index),
    path('add',views.add)

]