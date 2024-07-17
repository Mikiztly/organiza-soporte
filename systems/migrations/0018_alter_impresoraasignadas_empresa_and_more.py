# Generated by Django 5.0.6 on 2024-07-10 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0017_impresoraasignadas_empresa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impresoraasignadas',
            name='Empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='systems.sucursal'),
        ),
        migrations.AlterField(
            model_name='impresoraasignadas',
            name='Equipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='systems.equipo'),
        ),
        migrations.AlterField(
            model_name='impresoraasignadas',
            name='Impresora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='systems.impresora'),
        ),
    ]
