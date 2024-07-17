from django.contrib import admin
from .forms import EquipoForm, ImpresoraForm, ImpresoraAsignadasForm
from systems.models import Empresa, Sucursal, Equipo, Impresora, Departamento, Correos, Documentacion, ImpresoraAsignadas


class EquipoAdmin(admin.ModelAdmin):
    form = EquipoForm
    list_display = ('Tipo', 'Equipo', 'Marca', 'Serie', 'Area', 'Sucursal', 'Usuario', 'SO', 'Estado')
    search_fields = ('Tipo', 'Equipo', 'Marca', 'Serie', 'Usuario', 'SO', 'Estado')
    list_filter = ('Tipo', 'Marca', 'SO', 'Estado', 'Sucursal', 'Area')


class ImpresoraAdmin(admin.ModelAdmin):
    form = ImpresoraForm
    list_display = ('id', 'Empresa', 'Ubicacion', 'Modelo', 'Ip')
    search_fields = ('id', 'Empresa', 'Ubicacion', 'Modelo', 'Ip')
    list_filter = ('Empresa', 'Ip')


class ImpresorasAsignadasAdmin(admin.ModelAdmin):
    form = ImpresoraAsignadasForm
    list_display = ('Empresa', 'Equipo', 'Impresora')


# Register your models here.
admin.site.register(Empresa)
admin.site.register(Sucursal)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Impresora, ImpresoraAdmin)
admin.site.register(ImpresoraAsignadas, ImpresorasAsignadasAdmin)
admin.site.register(Departamento)
admin.site.register(Correos)
admin.site.register(Documentacion)