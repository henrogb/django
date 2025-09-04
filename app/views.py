from django.shortcuts import render
from django.http import HttpResponse

def app_menu(request):
    return HttpResponse("rota app novo")

def exemplo(request):
    return HttpResponse("só é acessivel dentro do app novo")
