# Generated by Django 5.0.6 on 2024-07-23 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0021_alter_impresora_empresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='impresora',
            old_name='Empresa',
            new_name='Sucursal',
        ),
    ]
