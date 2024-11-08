# Generated by Django 5.0.6 on 2024-08-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0027_alter_comentarioequipo_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='creado_por',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='equipo',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='sucursal',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='prioridad',
            field=models.CharField(choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta'), ('Crítica', 'Crítica')], default='Baja', max_length=10),
        ),
    ]
