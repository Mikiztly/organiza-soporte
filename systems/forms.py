from django import forms
from .models import Equipo, Impresora
from django_select2.forms import Select2MultipleWidget


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'Tipo': forms.Select(choices=[
                ('Notebook', 'Notebook'),
                ('PC', 'PC de Escitorio'),
            ]),
            'SO': forms.Select(choices=[
                ('Windows 10 PRO 64', 'Windows 10 PRO 64'),
                ('Windows 11 PRO 64', 'Windows 11 PRO 64'),
                ('Windows 10 HOME 64', 'Windows 10 HOME 64'),
                ('Windows 11 HOME 64', 'Windows 11 HOME 64')

            ]),
            'Estado': forms.Select(choices=[
                ('Asignado', 'Asignado a un usuario'),
                ('Sin Asignar', 'Sin Asignar'),
                ('Reparacion', 'En Reparacion')
            ]),
            'correo': Select2MultipleWidget(),
        }


class ImpresoraForm(forms.ModelForm):
    class Meta:
        model = Impresora
        fields = '__all__'
        widgets = {
            'Empresa': forms.Select(choices=[
                (1, "NBC-EspaÃ±a"),
                (3, "Salta - Capital"),
                (4, "NBC-Ohiggins"),
                (5, "Central"),
                (6, "Enterprise"),
                (7, "IDS Seguridad"),
                (8, "Cafayate"),
                (9, "Metan"),
                (10, "JVG"),
                (11, "Oran"),
                (12, "Tartagal"),
                (13, "Rosario de la Frontera"),
                (14, "Guemes"),
                (15, "Strong Systems"),
            ])
        }
