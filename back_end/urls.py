"""
URL configuration for back_end project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #aqui o include serve para puxar as views de outros apps
#importar o httpresponse
from django.http import HttpResponse
#importar as views do arquivo views
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # ai é necessário colocar o views.nome_da_função(view)
    path('teste/', views.teste_view),
    path('', views.padrao),
    path('app/', include('app.urls'))
]
