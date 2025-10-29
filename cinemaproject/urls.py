from django.contrib import admin
from django.urls import include, path

#esta direccion apunta a las urls de cinemaapp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cinemaapp/', include('cinemaapp.urls'))
]
