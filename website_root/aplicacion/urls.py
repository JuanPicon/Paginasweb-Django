from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name="index"),
    path('Quienes_somos.html',views.index,name="index"),
    path('Servicios.html',views.Servicios,name="Servicios"),
    path('Catalogo.html',views.Catalogo,name="Catalogo"),
    path('Contacto.html',views.Contacto,name="Contacto"),
]