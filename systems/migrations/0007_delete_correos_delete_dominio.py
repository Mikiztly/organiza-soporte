# Generated by Django 5.0.6 on 2024-06-24 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0006_departamento_dominio_alter_equipo_area_correos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Correos',
        ),
        migrations.DeleteModel(
            name='Dominio',
        ),
    ]
