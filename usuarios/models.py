#Models são objetos que representam as tabelas do banco de dados
#Ao iniciar um projeto Django, nos é dado um db sqlite, e todos os models irão para lá por padrão
#Ao criar um model, faça um makemigrations e migrate para que ele seja criado no banco de dados

from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    #auto_now_add define que a data será preenchida automaticamente com a data atual na criação do objeto
    #null=True permite que o campo seja nulo no banco de dados
    dataCriacao = models.DateField(auto_now_add=True, null=True)