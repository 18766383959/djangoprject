from django.contrib import admin
from django.urls import path, include

from web import views

urlpatterns = [
    path('web1/',views.web),

]

app_name = 'learning_logs'