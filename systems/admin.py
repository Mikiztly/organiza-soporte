from django.urls import reverse
from django.contrib import admin
from django.utils.safestring import mark_safe
from .forms import EquipoForm, ImpresoraForm, ImpresoraAsignadasForm, ComentarioEquipoForm
from systems.models import Empresa, Sucursal, Equipo, Impresora, Departamento, Correos, Documentacion, ImpresoraAsignadas, Ticket, Comentario, ComentarioEquipo


class ComentarioEquipoInline(admin.TabularInline):
    model = ComentarioEquipo
    form = ComentarioEquipoForm
    extra = 1
    fields = ('contenido', 'fecha_creacion', )
    readonly_fields = ('fecha_creacion',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(ComentarioEquipoInline, self).get_formset(request, obj, **kwargs)
        formset.form = self.form
        formset.user = request.user
        return formset

@admin.register(ComentarioEquipo)
class ComentarioEquipoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'autor', 'fecha_creacion')
    search_fields = ('equipo__Usuario', 'contenido')


class EquipoAdmin(admin.ModelAdmin):
    form = EquipoForm
    list_display = ('Tipo', 'Equipo', 'Marca', 'Serie', 'Area', 'Sucursal', 'Usuario', 'SO', 'Estado')
    search_fields = ('Tipo', 'Equipo', 'Marca', 'Serie', 'Usuario', 'SO', 'Estado')
    list_filter = ('Tipo', 'Marca', 'SO', 'Estado', 'Sucursal', 'Area')
    inlines = [ComentarioEquipoInline]


class ImpresoraAdmin(admin.ModelAdmin):
    form = ImpresoraForm
    list_display = ('id', 'Sucursal', 'Ubicacion', 'Modelo', 'Ip')
    search_fields = ('id', 'Sucursal', 'Ubicacion', 'Modelo', 'Ip')
    list_filter = ('Sucursal', 'Ip')


class ImpresorasAsignadasAdmin(admin.ModelAdmin):
    form = ImpresoraAsignadasForm
    list_display = ('Empresa', 'Equipo', 'Impresora')
    search_fields = ('Empresa', 'Equipo', 'Impresora')
    list_filter = ('Empresa', 'Equipo', 'Impresora')

    class Media:
        js = ('assets/js/admin_dependant_selects.js',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name in ["Equipo", "Impresora"]:
            kwargs["queryset"] = db_field.related_model.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['Empresa'].widget.attrs.update({
            'data-ajax-url': reverse('filter_equipos')
        })
        return super().render_change_form(request, context, *args, **kwargs)


# Register your models here.
admin.site.register(Empresa)
admin.site.register(Sucursal)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Impresora, ImpresoraAdmin)
admin.site.register(ImpresoraAsignadas, ImpresorasAsignadasAdmin)
admin.site.register(Departamento)
admin.site.register(Correos)
admin.site.register(Documentacion)
admin.site.register(Ticket)
admin.site.register(Comentario)
