# Generated by Django 5.0.6 on 2024-06-27 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0012_rename_correo_equipo_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='correos',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='systems.empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='correos',
            name='estado',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]
