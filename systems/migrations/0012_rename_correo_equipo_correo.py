# Generated by Django 5.0.6 on 2024-06-25 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0011_alter_equipo_correo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='Correo',
            new_name='correo',
        ),
    ]
