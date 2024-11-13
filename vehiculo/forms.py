from django import forms
from .models import Vehiculo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #para agregar estilos de bootstrap según el tipo de input
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        
        self.fields['marca'].widget.attrs['class'] = 'form-select'
        self.fields['categoria'].widget.attrs['class'] = 'form-select'
        
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})        
