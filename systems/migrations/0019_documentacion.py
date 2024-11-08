# Generated by Django 5.0.6 on 2024-07-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0018_alter_impresoraasignadas_empresa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=16)),
                ('descripcion', models.TextField()),
                ('documento', models.FileField(upload_to='source/documentacion')),
            ],
            options={
                'verbose_name': 'Documentacion',
                'verbose_name_plural': 'Documentacion',
            },
        ),
    ]
