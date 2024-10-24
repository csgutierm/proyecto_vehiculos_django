from django.urls import path
from .views import  VehiculoCreateView
from . import views

app_name = 'vehiculo'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', VehiculoCreateView.as_view(), name='add'),
]
