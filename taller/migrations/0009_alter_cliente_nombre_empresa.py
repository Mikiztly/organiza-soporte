# Generated by Django 5.0.6 on 2024-10-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taller', '0008_alter_cliente_nombre_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombre_empresa',
            field=models.CharField(blank=True, choices=[('Particular', 'Particular'), ('Nubicom', 'Nubicom'), ('Strong', 'Strong'), ('IDS', 'IDS'), ('Enterprise', 'Enterprise')], default='0', max_length=20, null=True),
        ),
    ]
