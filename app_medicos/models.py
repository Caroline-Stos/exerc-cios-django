from django.db import models

#Caroline Santos

class Especialidade(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=300)

class Medicos(models.Model):
    name = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15, default='')  
    email = models.EmailField(max_length=200)
    nascimento = models.DateField(auto_now=False, auto_now_add=False)
    crm = models.CharField(max_length=10, default='')  
    especialidade = models.ForeignKey('Especialidade', on_delete=models.CASCADE)

