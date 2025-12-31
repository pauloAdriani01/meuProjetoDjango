'''
Views do Django são funções ou classe em python que recebem requisições http e retornam respostas http, como página html

*HTTP -> HyperText Transfer Protocol é o protocolo de comunicação utilizado na web para transferir dados entre cliente e servidor.
'''

from django.shortcuts import render

#Biblioteca HttpResponse permite criar respostas HTTP personalizadas
from django.http import HttpResponse

#Importa o template loader do Django, que carrega templates HTML
from django.template import loader

def index(request):
    #Importa o template loader do Django e envia o meu template para a url quando solicitado
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
