# Generated by Django 5.0.6 on 2024-07-15 16:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0019_documentacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentacion',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]