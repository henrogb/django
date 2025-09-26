#arquivo para criar as views 
from django.http import HttpResponse
from django.shortcuts import render

def teste_view(request):
    return HttpResponse("rota de teste")

def padrao(request):
    return HttpResponse("Bem vindo")
