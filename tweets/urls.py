from django.contrib import admin
from django.urls import path

from django.http import HttpResponse


from . import views


urlpatterns = [
    path('<str:handle>/', views.homeWithHandle),
    path('user/<str:handle>/', views.homeWithHandle),
    path('', views.home),
    path('pages/about/', views.about),
    path('pages/error/', views.error),
]
