# Generated by Django 5.0.6 on 2024-06-24 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0007_delete_correos_delete_dominio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='Area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='systems.departamento'),
        ),
    ]
