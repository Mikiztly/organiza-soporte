from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="taller"),
    path("orden-reparacion", views.ordenReparacion, name="orden-reparacion"),
    path('filtrar-equipos/', views.filtrar_equipos_por_cliente, name='filtrar_equipos_por_cliente'),
    path('obtener-cliente/', views.obtener_cliente_por_equipo, name='obtener_cliente_por_equipo'),
    path('ListaOrdenReparacion', views.ListaOrdenReparacion, name='ListaOrdenReparacion'),
    path('Orden/<int:pk>/', views.DetalleOrdenReparacion.as_view(), name='detalleOrdenReparacion'),
    path('cliente/notificar/<int:id>/', views.notificaciones_cliente, name='enviar_notificacion_cliente'),
]
