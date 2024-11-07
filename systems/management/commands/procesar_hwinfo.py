from django.core.management.base import BaseCommand
from systems.utils import leer_hwinfo_xml  # Asegúrate de ajustar la ruta correcta


class Command(BaseCommand):
    help = 'Lee archivos XML de HWInfo y actualiza o agrega equipos'

    def add_arguments(self, parser):
        parser.add_argument('archivo_xml', type=str, help='source/hwinfo')

    def handle(self, *args, **kwargs):
        archivo_xml = kwargs['archivo_xml']
        equipo = leer_hwinfo_xml(archivo_xml)
        self.stdout.write(self.style.SUCCESS(f'Equipo {equipo.nombre} procesado exitosamente.'))
