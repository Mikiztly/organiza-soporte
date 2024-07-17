from django.db import models


class Empresa(models.Model):
    Nombre = models.CharField(max_length=100)
    #Estado = models.CharField(max_length=10)
    #Inicial = models.CharField(max_length=10)

    def __str__(self):
        return self.Nombre


class Sucursal(models.Model):
    Empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    Nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Empresa}  {self.Nombre}'

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursal'


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


class Correos(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    email_address = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.email_address


class Equipo(models.Model):
    Tipo = models.CharField(max_length=100)
    Equipo = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100, null=True, blank=True)
    Serie = models.CharField(max_length=100, unique=1)
    Area = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True, blank=True)

    Sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    Usuario = models.CharField(max_length=100, null=True, blank=True)
    correo = models.ManyToManyField(Correos, blank=True)
    SO = models.CharField(max_length=100, null=True, blank=True)
    Microprocesador = models.CharField(max_length=100, null=True, blank=True)
    MemoriaRam = models.CharField(max_length=100, null=True, blank=True)
    Disco = models.CharField(max_length=100, null=True, blank=True)
    Discoserie = models.CharField(max_length=100, null=True, blank=True)
    PlacaGrafica = models.CharField(max_length=100, null=True, blank=True)
    Observaciones = models.CharField(max_length=100, null=True, blank=True)
    Estado = models.CharField(max_length=100, null=True, blank=True)
    IP = models.CharField(max_length=100, null=True, blank=True)
    Monitor_1 = models.CharField(max_length=100, null=True, blank=True)
    MonitorSN_1 = models.CharField(max_length=100, null=True, blank=True)
    Monitor_2 = models.CharField(max_length=100, null=True, blank=True)
    MonitorSN_2 = models.CharField(max_length=100, null=True, blank=True)
    Monitor_3 = models.CharField(max_length=100, null=True, blank=True)
    MonitorSN_3 = models.CharField(max_length=100, null=True, blank=True)
    Monitor_4 = models.CharField(max_length=100, null=True, blank=True)
    MonitorSN_4 = models.CharField(max_length=100, null=True, blank=True)
    Observacion_perifericos = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.Usuario} {self.Sucursal}'


class Impresora(models.Model):
    Nombre = models.CharField(max_length=100)
    Modelo = models.CharField(max_length=100, null=True, blank=True)
    Ip = models.GenericIPAddressField()
    MacAddress = models.CharField(max_length=100, null=True, blank=True)
    Ubicacion = models.CharField(max_length=100, null=True, blank=True)
    Empresa = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.Nombre} {self.Ubicacion}'


class ImpresoraAsignadas(models.Model):
    Empresa = models.ForeignKey(Sucursal, on_delete=models.PROTECT, null=True, blank=True)
    Equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT, null=True, blank=True)
    Impresora = models.ForeignKey(Impresora, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.Equipo} - {self.Impresora}'


class Documentacion(models.Model):
    titulo = models.CharField(max_length=16)
    descripcion = models.TextField()
    documento = models.FileField(upload_to='source/documentacion')
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.titulo} {self.descripcion}'

    class Meta:
        verbose_name = 'Documentacion'
        verbose_name_plural = 'Documentacion'



