from django.urls import path
from . import views


urlpatterns = [
    path('', views.app_menu),
    path('novaview', views.exemplo)
]