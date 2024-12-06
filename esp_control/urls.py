# esp_control/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.controle_home, name='controle_home'),
    path('ligar/', views.ligar, name='ligar'),
    path('desligar/', views.desligar, name='desligar'),
    path('ajustar_temperatura/<int:temp>/', views.ajustar_temperatura, name='ajustar_temperatura'),
    path('verificar_conexao/', views.verificar_conexao, name='verificar_conexao'),  # Nova rota
]
