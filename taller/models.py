from django.db import models


class Cliente(models.Model):
    EMPRESAS = [("Particular", "Particular"), ("Nubicom", 'Nubicom'), ("Strong", 'Strong'), ("IDS", 'IDS'), ("Enterprise", 'Enterprise')]
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    empresa = models.BooleanField(default=False, blank=True, null=True)
    nombre_empresa = models.CharField(max_length=20, choices=EMPRESAS, blank=True, null=True, default='0')
    cuit = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_empresa} - {self.nombre}  {self.apellido}"


class Equipo(models.Model):
    Tipo = [(1, 'Desktop'), (2, 'Notebook'), (3, 'All in one'), (4, 'Impresora')]
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=Tipo, blank=True, null=True)  # Ejemplo: Laptop, Desktop, etc.
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    numero_serie = models.CharField(max_length=50, unique=True)  # Campo para el número de serie
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='equipos')
    hostname = models.CharField(max_length=50, blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return f"cod:{self.id} -{self.modelo}"


class OrdenReparacion(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
        ('entregado', 'Equipo entregado' )
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='ordenes', blank=True, null=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT, related_name='ordenes', blank=True, null=True)
    falla = models.TextField(blank=True, null=True)
    accesorios = models.CharField(max_length=255, blank=True, null=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_estimada = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    informe_tecnico = models.TextField(blank=True, null=True)  # Informe técnico sobre la reparación

    # Nuevos campos para el informe del cliente y precios
    informe_cliente = models.TextField(blank=True, null=True)  # Informe final para el cliente
    precio_mano_obra = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    precio_repuestos = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    iva = models.DecimalField(max_digits=5, decimal_places=2, default=21.00, blank=True, null=True)  # IVA (21%)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)

    def calcular_total(self):
        subtotal = self.precio_mano_obra + self.precio_repuestos
        total_con_iva = subtotal + (subtotal * (self.iva / 100))
        return total_con_iva

    def save(self, *args, **kwargs):
        self.total = self.calcular_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Orden #{self.id} para {self.equipo} de {self.cliente}"


