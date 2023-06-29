
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
     path('', views.resetpassword, name=''),
     path('submit', views.submit, name='submit'),
]
