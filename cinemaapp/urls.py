from django.contrib import admin
from django.urls import path
from cinemaapp import views

# aquí decimos que termine la ruta en form/
urlpatterns = [
    path('form/', views.form, name = "form"),
]