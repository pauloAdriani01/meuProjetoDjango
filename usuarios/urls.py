#Bibliotecas importadas para configuração de URLs

from django.urls import path #Importa a função path para definir rotas de URL
from . import views #Importa o módulo views do diretório atual

urlpatterns = [
    #Define a rota /usuarios que chama a função usuarios na views.py
    #Com um caminho vazio, ele mostra a view automaticamente
    path('', views.index, name='index'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('detalhes/<int:id>/', views.detalhes, name='detalhes')

]