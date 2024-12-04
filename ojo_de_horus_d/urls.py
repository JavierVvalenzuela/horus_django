from django.contrib import admin
from django.urls import path, include  # Usas include para incluir las URLs de la app "foro"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foro.urls')),  # Aquí rediriges a las URLs de la app "foro"
]
