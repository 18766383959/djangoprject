from django.contrib import admin
from django.urls import path, include

from learning_logs import views

urlpatterns = [
    path('zy/',views.index,name= 'index'),
    path('topic/',views.topics,name = 'topics')
]

app_name = 'learning_logs'