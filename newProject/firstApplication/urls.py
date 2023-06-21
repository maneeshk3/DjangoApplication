
from django.contrib import admin
from django.urls import path
from firstApplication import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name = "about"),
    path("service", views.service, name = "service")
]
