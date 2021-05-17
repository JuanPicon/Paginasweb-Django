from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'Quienes_somos.html')

def Servicios(request):
    return render(request, 'Servicios.html')

def Catalogo(request):
    return render(request, 'Catalogo.html')

def Contacto(request):
    return render(request, 'Contacto.html')
