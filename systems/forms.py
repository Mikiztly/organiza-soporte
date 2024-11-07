from django import forms
from django.shortcuts import get_object_or_404

from .models import Equipo, Impresora, Sucursal, ImpresoraAsignadas, Documentacion, ComentarioEquipo
from django_select2.forms import Select2MultipleWidget


class ImpresoraForm(forms.ModelForm):
    #Empresa = forms.ModelChoiceField(queryset=Sucursal.objects.all())

    class Meta:
        model = Impresora
        fields = '__all__'


class ImpresoraAsignadasForm(forms.ModelForm):
    Empresa = forms.ModelChoiceField(queryset=Sucursal.objects.all())
    Equipo = forms.ModelChoiceField(queryset=Equipo.objects.none())  # Inicialmente vacío
    Impresora = forms.ModelChoiceField(queryset=Impresora.objects.none())  # Inicialmente vacío

    class Meta:
        model = ImpresoraAsignadas
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs and kwargs['instance']:
            empresa = kwargs['instance'].Empresa
            self.fields['Equipo'].queryset = Equipo.objects.filter(Sucursal=empresa)
            self.fields['Impresora'].queryset = Impresora.objects.filter(Sucursal=empresa)
        elif 'data' in kwargs and 'Empresa' in kwargs['data']:
            empresa_id = int(kwargs['data']['Empresa'])
            self.fields['Equipo'].queryset = Equipo.objects.filter(Sucursal_id=empresa_id)
            self.fields['Impresora'].queryset = Impresora.objects.filter(Sucursal_id=empresa_id)
        else:
            self.fields['Equipo'].queryset = Equipo.objects.all()
            self.fields['Impresora'].queryset = Impresora.objects.all()


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


class ComentarioEquipoForm(forms.ModelForm):
    class Meta:
        model = ComentarioEquipo
        fields = ['contenido']  # No incluimos 'autor', se asignará automáticamente

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ComentarioEquipoForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ComentarioEquipoForm, self).save(commit=False)
        if self.user:
            instance.autor = self.user
        if commit:
            instance.save()
        return instance
