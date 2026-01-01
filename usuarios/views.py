'''
Views do Django são funções ou classe em python que recebem requisições http e retornam respostas http, como página html

*HTTP -> HyperText Transfer Protocol é o protocolo de comunicação utilizado na web para transferir dados entre cliente e servidor.
'''

from django.shortcuts import render

#Biblioteca HttpResponse permite criar respostas HTTP personalizadas
from django.http import HttpResponse

#Importa o template loader do Django, que carrega templates HTML
from django.template import loader

#Importa a tabela Usuario do arquivo models.py
from .models import Usuario

def usuarios(request):
    #Obtem todos os objetos do model Usuario
    usuarios = Usuario.objects.all().values() 

    #Importa o template loader do Django e envia o meu template para a url quando solicitado
    template = loader.get_template('usuarios.html')

    context = {
        'usuarios': usuarios

    }

    return HttpResponse(template.render(context, request))

def detalhes(request, id):
    usuario = Usuario.objects.get(id=id)

    template = loader.get_template('detalhes.html')

    context = {
        'usuario': usuario
    }

    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('index.html')

    return HttpResponse(template.render())


