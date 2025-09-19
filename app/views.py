from django.shortcuts import render
from django.http import HttpResponse


#então o q acontece aqui é que estamos criando um caminho para acessar o arquivo html
#importamos e usamos o render com os dois argumentos request e o caminho até o arquivo
#interessante ressaltar q por termos configurado o dir no templates de settings ele 
#irá puxar todos os arquivos que encontrar na pasta templates 
def app_menu(request):
    return render(request, 'menu/validacao.html')

def exemplo(request):
    return HttpResponse("só é acessivel dentro do app novo")
