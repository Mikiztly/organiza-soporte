from .models import Empresa, Documentacion, Equipo


def getListas_template(request):
    equipos = Equipo.objects.all()
    empresas = Empresa.objects.all().prefetch_related('sucursal_set')
    documentacion = Documentacion.objects.all()
    context = {
        'get_empresas': empresas, 'get_equipos': equipos, 'get_documentacion': documentacion
    }
    return context
