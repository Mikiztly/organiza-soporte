from django import forms
from django_select2.forms import Select2Widget
from .models import OrdenReparacion, Cliente, Equipo
from django.forms import TextInput, Textarea


class OrdenReparacionForm(forms.ModelForm):
    class Meta:
        model = OrdenReparacion
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(
                attrs={'class': 'form-control', 'id': 'cliente-select', 'aria-describedby': 'addClienteButton'}),
            'equipo': forms.Select(
                attrs={'class': 'form-control', 'id': 'equipo-select', 'aria-describedby': 'addEquipoButton'}),
            'falla': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe la falla del equipo'}),
            'accesorios': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Accesorios entregados'}),
            'precio_mano_obra': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Precio de mano de obra'}),
            'precio_repuesto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio de repuestos'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'IVA'}),
            'estado': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Selecciona el estado de la reparación'}),
            'informe_tecnico': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Informe técnico'}),
            'informe_cliente': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Informe para el cliente'}),
        }


class edit_OrdenReparacionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Deshabilitar los campos 'cliente' y 'equipo'
        self.fields['cliente'].readonly = True
        self.fields['equipo'].readonly = True

    class Meta:
        model = OrdenReparacion
        fields = '__all__'
