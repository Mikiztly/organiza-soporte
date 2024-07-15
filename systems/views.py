from dal import autocomplete
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Equipo, Empresa, Sucursal
from django.views.generic.detail import DetailView
from django.template.loader import get_template, TemplateDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
#from .models import SystemInfo, DiskInfo

# Create your views here.
def index(request):
    equipos = Equipo.objects.all()
    empresas = Empresa.objects.all().prefetch_related('sucursal_set')
    context = {
        'empresas': empresas, 'equipos': equipos
    }
    return render(request, "index.html", context)


def ListaFiltada(request, emp, Nombre, id):
    equipos = Equipo.objects.filter(Sucursal=id)
    #print(equipos)
    empresas = Empresa.objects.all().prefetch_related('sucursal_set')
    context = {
        'equipos': equipos,
        'empresas': empresas,
        'sucursal_actual_id': id,  # Pasar el id de la sucursal actual
        'activeSucusal': Nombre,
        'showEmpresa': emp

    }
    #print(context)
    return render(request, "empresa/lista_empresa.html", context)


def viewEquipo(request):
    return render(request, "equipo.html")


def EquipoDetailView(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    empresas = Empresa.objects.all().prefetch_related('sucursal_set')
    impresora = Empresa.objects.all().prefetch_related('impresora_set')
    context = {
        'equipo': equipo, 'empresas': empresas
    }
    return render(request, 'equipo.html', context)


#csrf_exempt elimina las restricciones en esa vista
#@csrf_exempt
def systems_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        return JsonResponse({'status': 'success'}, status=201)
    return JsonResponse({'status': 'error'}, status=400)
