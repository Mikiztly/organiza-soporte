from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .forms import OrdenReparacionForm, edit_OrdenReparacionForm
from .models import Equipo, Cliente, OrdenReparacion
from django.views.generic import DetailView, UpdateView


def index(request):
    # Define el contexto correctamente como un diccionario
    context = {"mje": "Orden de reparacion"}
    return render(request, "taller/index.html", context)


def ordenReparacion(request):
    if request.method == 'POST':
        form = OrdenReparacionForm(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['cliente']
            equipo = form.cleaned_data['equipo']
            if not cliente or not equipo:
                messages.error(request, 'Cliente y Equipo son obligatorios')
                context = {"form": form, "mje": "Orden de reparación"}
                return render(request, "taller/ordenReparacion.html", context)
            form.save()  # Guardar la orden de reparación en la base de datos
            id = OrdenReparacion.objects.count()
            messages.success(request, f"Orden N° {id}: Se agrego una orden de reparacion")
            return redirect('ListaOrdenReparacion')  # Redirigir después de guardar
    else:
        form = OrdenReparacionForm()

    context = {"form": form, "mje": "Orden de reparación"}
    return render(request, "taller/ordenReparacion.html", context)


def ListaOrdenReparacion(request):
    ordenes = OrdenReparacion.objects.all()  # Obtén todas las órdenes de reparación
    context = {
        "ordenes": ordenes
    }
    return render(request, 'taller/listaorndenreparacion.html', context)


class DetalleOrdenReparacion(UpdateView):
    model = OrdenReparacion
    form_class = OrdenReparacionForm
    template_name = 'taller/detalle_orden_reparacion.html'
    # context_object_name = 'orden'
    success_url = reverse_lazy('ListaOrdenReparacion')  # Redirigir a la lista de órdenes después de guardar

    def get_success_url(self):
        # Redirige a la misma página después de guardar los cambios
        return reverse('detalleOrdenReparacion', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.cliente = self.get_object().cliente
        self.object.equipo = self.get_object().equipo
        self.object.save()  # Guardar cambios con cliente y equipo preservados
        form.save()
        messages.success(self.request, "Cambios guardados")
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si el formulario es inválido, lo volvemos a renderizar con los errores
        print("Errores en el formulario:", form.errors)
        return self.render_to_response(self.get_context_data(form=form))


def filtrar_equipos_por_cliente(request):
    cliente_id = request.GET.get('cliente_id')
    equipos = Equipo.objects.filter(cliente_id=cliente_id).values('id', 'nombre')
    return JsonResponse(list(equipos), safe=False)


def obtener_cliente_por_equipo(request):
    equipo_id = request.GET.get('equipo_id')  # Obtener el ID del equipo desde la solicitud AJAX
    equipo = Equipo.objects.get(id=equipo_id)  # Buscar el equipo por su ID
    cliente = equipo.cliente  # Obtener el cliente relacionado con el equipo
    return JsonResponse({'cliente_id': cliente.id, 'cliente_nombre': cliente.nombre})


def buscar_cliente(request):
    search_term = request.GET.get('search_term', '')
    clientes = Cliente.objects.filter(nombre__icontains=search_term) | Cliente.objects.filter(id=search_term)

    # Devuelve una lista de clientes en formato JSON
    data = [{'id': cliente.id, 'nombre': cliente.nombre} for cliente in clientes]
    return JsonResponse(data, safe=False)


def buscar_equipo(request):
    equipo_id = request.GET.get('equipo_id', '')
    equipos = Equipo.objects.filter(numero_serie__icontains=equipo_id)

    # Devuelve una lista de equipos en formato JSON
    data = [{'id': equipo.id, 'numero_serie': equipo.numero_serie} for equipo in equipos]
    return JsonResponse(data, safe=False)


def notificaciones(recipient_list, msge):
    destinatarios = ["candidornotar@gmail.com", "candidornotar@yahoo.com", "candidornotar@hotmail.com",
                     "candidornotar@outlook.com", "admin@jethro.com.ar", "admin@candidornotar.com.ar",
                     "pablo.baldivieso@outlook.com"]

    try:
        send_mail(
            "Notificaciones",
            f'{msge}',
            None,
            # recipient_list,  # Correos del cliente a enviar.
            destinatarios,  # correos fijos de prueba.
            fail_silently=False,
        )
        print('Notificado por correo')
        return True
    except Exception as e:
        print(f"Error al enviar el correo: {str(e)}")  # Error en consola


def notificaciones_cliente(request, id):
    lista = []
    ordenReparacion = get_object_or_404(OrdenReparacion, pk=id)
    cliente = get_object_or_404(Cliente, pk=ordenReparacion.cliente_id)
    informe = ordenReparacion.informe_cliente
    equipo = ordenReparacion.equipo
    estado = ordenReparacion.estado
    fecha_estimada = ordenReparacion.fecha_estimada

    mensaje = f"""
        Estimado/a {cliente.nombre},

        Le informamos que la orden de reparación #{ordenReparacion.id} para su equipo {equipo} se encuentra en el estado: {estado}.

        Informe técnico:
        {informe if informe else "No se ha proporcionado un informe técnico todavía."}

        Fecha estimada de entrega: {fecha_estimada if fecha_estimada else "Fecha no disponible"}


        Si tiene alguna pregunta, no dude en contactarnos.

        Atentamente,
        El equipo de soporte técnico
        """

    if cliente.correo:
        lista.append(cliente.correo)
        enviado = notificaciones(lista, mensaje)
        if enviado:
            return redirect('ListaOrdenReparacion')
    else:
        print('no tiene correo')
