from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Vehiculo
from .forms import VehiculoForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'vehiculo/index.html')

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/vehiculo_form.html'
    #success_url = '/vehiculo/'
    success_url = reverse_lazy('vehiculo:index')
    
@login_required
def listar_vehiculos(request):
    vehiculos_bajos = Vehiculo.objects.filter(precio__lt=10000)
    vehiculos_medios = Vehiculo.objects.filter(precio__gte=10000, precio__lte=30000)
    vehiculos_altos = Vehiculo.objects.filter(precio__gt=30000)
    
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar_vehiculos.html', {
        'vehiculos': vehiculos,
        'vehiculos_bajos': vehiculos_bajos,
        'vehiculos_medios': vehiculos_medios,
        'vehiculos_altos': vehiculos_altos,
    })   
    
    
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso.")
            return redirect('vehiculo:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})    