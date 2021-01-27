from django.contrib import admin
from .models import Cliente,Celular

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','sexo','correo','n_telefono']
    search_fields = ['nombre']
    list_per_page = 15


class CelularAdmin(admin.ModelAdmin):
    list_display = ['marca','modelo','precio','cliente']
    search_fields = ['marca','modelo']
    list_filter = ['precio']
    list_per_page = 15



admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Celular,CelularAdmin)