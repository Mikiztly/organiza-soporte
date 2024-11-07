from django.shortcuts import render, get_object_or_404
from .models import Equipo, Empresa, Sucursal, ImpresoraAsignadas, Impresora, Documentacion, Ticket
from django.http import JsonResponse
import json


# Create your views here.
def index(request):
    equipos = Equipo.objects.all()
    empresas = Empresa.objects.all().prefetch_related('sucursal_set')
    documentacion = Documentacion.objects.all()
    context = {
        'empresas': empresas, 'equipos': equipos, 'documentacion': documentacion
    }
    return render(request, "index.html", context)


def ListaFiltada(request, emp, Nombre, id):
    equipos = Equipo.objects.filter(Sucursal=id)
    # print(equipos)
    empresas = Empresa.objects.all().prefetch_related('sucursal_set')
    context = {
        'equipos': equipos,
        'empresas': empresas,
        'sucursal_actual_id': id,  # Pasar el id de la sucursal actual
        'activeSucusal': Nombre,
        'showEmpresa': emp

    }
    # print(context)
    return render(request, "empresa/lista_empresa.html", context)


def viewEquipo(request):
    return render(request, "equipo.html")


def EquipoDetailView(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    # impresoras = Impresora.objects.filter(sucursal_actual_id=id)
    empresas = Empresa.objects.all().prefetch_related('sucursal_set')
    # impresora = Empresa.objects.all().prefetch_related('impresora_set')
    # Reemplaza 'some_equipo_id' con el id del equipo de interés
    # impresoras_asignadas = ImpresoraAsignadas.objects.filter(Equipo_id=id)
    # impresoras = [imp_asignada.Impresora for imp_asignada in impresoras_asignadas]

    context = {
        'equipo': equipo, 'empresas': empresas  # , #'impresoras_asignadas': impresoras
    }
    return render(request, 'equipo.html', context)


# Documentacion vistas
def listDocumentacion(request):
    documentacion = Documentacion.objects.all()
    context = {
        'documentacion': documentacion
    }
    return render(request, 'documentacion/index.html', context)


def viewDocumento(request, id):
    documento = get_object_or_404(Documentacion, id=id)
    context = {
        'documento': documento
    }
    return render(request, 'documentacion/pdf.html', context)


# -------------------------

# csrf_exempt elimina las restricciones en esa vista
# @csrf_exempt
def systems_info(request):  # funcion par ver la informacion por medio de un agente.py
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        return JsonResponse({'status': 'success'}, status=201)
    return JsonResponse({'status': 'error'}, status=400)


##########Asinacion de impresoras###################

def filter_equipos(request):
    sucursal_id = request.GET.get('sucursal_id')
    equipos = Equipo.objects.filter(Sucursal_id=sucursal_id).values('id', 'Equipo')
    impresoras = Impresora.objects.filter(Sucursal_id=sucursal_id).values('id', 'Nombre')
    data = {
        'equipos': list(equipos),
        'impresoras': list(impresoras)
    }
    print("paso por viewFilter_equipos")
    print(data)
    return JsonResponse(data)
    # return JsonResponse(list(equipos), list(impresoras), safe=False)


# Vista de grafico
def dashboard(request):
    sucursales_data = []
    data = []
    labels = []

    # Iterar sobre todas las sucursales
    for sucursal in Sucursal.objects.all():
        cantidad_items = Equipo.objects.filter(Sucursal=sucursal).count()
        if cantidad_items > 0:  # Considerar solo las sucursales con equipos
            sucursales_data.append({
                'id': sucursal.id,
                'nombre': sucursal.Nombre,
                'cantidad_items': cantidad_items
            })
            # Concatenar nombre de la empresa y sucursal para el label
            label = f"{sucursal.Empresa.Nombre} - {sucursal.Nombre}"
            labels.append(label)
            data.append(cantidad_items)
    total = Equipo.objects.all().count()

    context = {
        'sucursales_data': sucursales_data,
        'data': data,
        'labels': labels,
        'total': total,
    }

    print(total)  # Imprimir los datos para depuración

    return render(request, 'dashboard.html', context)


# CRUD DE TICKETS !
def ticketsViews(request):
    tickets = Ticket.objects.all()
    context = {
        'text': 'texto de inicio',
        'tickets': tickets
    }
    return render(request, 'tickets/index.html', context)


def ticketsDetailView(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    msg = ' Este es un ticket de prueba'
    context = {
        'ticket': ticket,
    }
    return render(request, 'tickets/ticket.html', context)



