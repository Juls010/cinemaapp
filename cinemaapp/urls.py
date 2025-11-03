from django.contrib import admin
from django.urls import path
from cinemaapp import views

# aquí decimos que termine la ruta en form/
urlpatterns = [
    path('form/', views.form, name = "form"),
    path('<int:pk>/edit/', views.movie_edit, name = "movie_edit"),
    path('list', views.movie_list, name='movie_list')
]