from django.urls import path
from .views import  VehiculoCreateView
from . import views

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

app_name = 'vehiculo'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', VehiculoCreateView.as_view(), name='add'),
    path('listar/', views.listar_vehiculos, name='listar'),
    path('test/', login_required(lambda request: HttpResponse("Usted se encuentra autenticado")), name='test'),
]
