from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.home1,name='results'),
    path('about/',views.about,name='about'),
    path('add/',views.add, name='add')
]
