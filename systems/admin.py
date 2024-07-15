from django.contrib import admin
from .forms import EquipoForm, ImpresoraForm
from systems.models import Empresa, Sucursal, Equipo, Impresora, ImpresoraAsignadas, Departamento, Correos


class EquipoAdmin(admin.ModelAdmin):
    form = EquipoForm
    list_display = ('Tipo', 'Equipo', 'Marca', 'Serie', 'Area', 'Sucursal', 'Usuario', 'SO', 'Estado')
    search_fields = ('Tipo', 'Equipo', 'Marca', 'Serie', 'Usuario', 'SO', 'Estado')
    list_filter = ('Tipo', 'Marca', 'SO', 'Estado', 'Sucursal', 'Area')


class ImpresoraAdmin(admin.ModelAdmin):
    form = ImpresoraForm


# Register your models here.
admin.site.register(Empresa)
admin.site.register(Sucursal)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Impresora)
admin.site.register(ImpresoraAsignadas)
admin.site.register(Departamento)
admin.site.register(Correos)