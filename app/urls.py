from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('', views.app_menu, name="home"),
    path('novaview', views.exemplo)
]