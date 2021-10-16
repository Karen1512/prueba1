from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def bienvenido(request): #reques peticion web que se envia al servidor de django
    return HttpResponse('Hola mundo') #salida a la pagina

def despedida(request):
    return HttpResponse('Hasta ta pronto!')
