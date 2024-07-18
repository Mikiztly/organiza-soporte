from django import forms
from django.shortcuts import get_object_or_404

from .models import Equipo, Impresora, Sucursal, ImpresoraAsignadas, Documentacion
from django_select2.forms import Select2MultipleWidget


class ImpresoraForm(forms.ModelForm):
    Empresa = forms.ModelChoiceField(queryset=Sucursal.objects.all())

    class Meta:
        model = Impresora
        fields = '__all__'


class ImpresoraAsignadasForm(forms.ModelForm):
    Empresa = forms.ModelChoiceField(queryset=Sucursal.objects.all())  # Inicialmente vacío
#    Equipo = forms.ModelChoiceField(queryset=Equipo.objects.filter(Sucursal=id))
    class Meta:
        model = ImpresoraAsignadas
        fields = '__all__'


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
