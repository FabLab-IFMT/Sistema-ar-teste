# esp_control/views.py
from django.shortcuts import render
import requests
from django.http import JsonResponse


ESP32_IP = 'http://192.168.1.114'  # IP do ESP32 na sua rede local

def controle_home(request):
    return render(request, 'controle.html')

def ligar(request):
    try:
        requests.post(f"{ESP32_IP}/ligar")  # Envia comando para o ESP32
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar comando: {e}")
    return render(request, 'controle.html', {'status': 'Comando enviado: Ligar'})

def desligar(request):
    try:
        requests.post(f"{ESP32_IP}/desligar")  # Envia comando para o ESP32
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar comando: {e}")
    return render(request, 'controle.html', {'status': 'Comando enviado: Desligar'})

def ajustar_temperatura(request, temp):
    try:
        requests.post(f"{ESP32_IP}/ajustar_temperatura", data={'temp': temp})  # Envia comando de ajuste de temperatura
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar comando: {e}")
    return render(request, 'controle.html', {'status': f'Comando enviado: Temperatura {temp}°C'})
def verificar_conexao(request):
    try:
        # Tentando acessar o ESP32 para verificar a conexão
        resposta = requests.get(f"{ESP32_IP}/status", timeout=2)  # Timeout de 2 segundos
        if resposta.status_code == 200:
            return JsonResponse({'conectado': True})  # Conectado
        else:
            return JsonResponse({'conectado': False})  # Não conectado
    except requests.exceptions.RequestException:
        return JsonResponse({'conectado': False})  # Erro, não conectado