from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.
def index(request):
    return render(request, 'vehiculo/index.html')

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/vehiculo_form.html'
    #success_url = '/vehiculo/'
    success_url = reverse_lazy('vehiculo:index')