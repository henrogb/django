#arquivo para criar as views 
from django.http import HttpResponse

def teste_view(request):
    return HttpResponse("rota de teste")

def padrao(request):
    return HttpResponse("Bem vindo")
