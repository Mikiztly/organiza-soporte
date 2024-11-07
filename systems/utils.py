import xml.etree.ElementTree as ET
from django.utils.dateparse import parse_datetime
from systems.models import Equipo  # Asegúrate de que la ruta sea correcta


def leer_hwinfo_xml(archivo_xml):
    tree = ET.parse(archivo_xml)
    root = tree.getroot()

    nombre_equipo = root.findtext('Computer Name', 'Desconocido')
    serial = root.findtext('System/SerialNumber', 'Desconocidaao')
    cpu = root.findtext('CPU/Name', 'Desconocido')
    ram = root.findtext('Memory/TotalMemory', 'Desconocido')

    equipo, creado = Equipo.objects.get_or_create(
        serial=serial,
        defaults={
            'nombre': nombre_equipo,
            'cpu': cpu,
            'ram': ram,
        }
    )

    if not creado:
        equipo.nombre = nombre_equipo
        equipo.cpu = cpu
        equipo.ram = ram
        equipo.save()

    return equipo
