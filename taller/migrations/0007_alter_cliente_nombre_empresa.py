# Generated by Django 5.0.6 on 2024-10-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0006_cliente_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombre_empresa',
            field=models.CharField(blank=True, choices=[('Nubicom', 'Nubicom'), ('Strong', 'Strong'), ('IDS', 'IDS'), ('Enterprise', 'Enterprise')], max_length=20, null=True),
        ),
    ]
