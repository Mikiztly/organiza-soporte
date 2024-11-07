from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("equipo", views.viewEquipo, name="equipo"),
    path('equipo/<int:id>/', views.EquipoDetailView, name='equipo_detail'),
    path("<str:emp>/<str:Nombre>/?<int:id>?0/", views.ListaFiltada, name='empresa_lista'),
    path("systems_info", views.systems_info, name="systems_info"),
    path("documentacion", views.listDocumentacion, name="documentacion"),
    path("documento/<int:id>", views.viewDocumento, name="documento"),
# otras urls
    path('ajax/filter_equipos/', views.filter_equipos, name='filter_equipos'),
    #path('impresoras/<int:sucursal_id>/', views.equipos_impresoras_lista, name='impresoras_por_sucursal'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('tickets', views.ticketsViews, name='tickets'),
    path('tickets/<int:id>', views.ticketsDetailView, name='tickets_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)