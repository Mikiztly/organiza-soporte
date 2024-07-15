from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("equipo", views.viewEquipo, name="equipo"),
    path('equipo/<int:id>/', views.EquipoDetailView, name='equipo_detail'),
    path("<str:emp>/<str:Nombre>/?<int:id>?0/", views.ListaFiltada, name='empresa_lista'),
    path("systems_info", views.systems_info, name="systems_info"),

]