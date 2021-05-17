from django.contrib import admin

from .models import Estanterías,Lockers,Muebles_de_oficina,Cajas_plásticas

# Register your models here.

admin.site.register(Estanterías)
admin.site.register(Lockers)
admin.site.register(Muebles_de_oficina)
admin.site.register(Cajas_plásticas)