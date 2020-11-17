from django.db import models
from django.utils import timezone

#Cada model é uma tabela no banco de dados
class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __self__(self):
        return self.nome


#Os atributos serão as colunas
class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __self__(self):
        return self.nome


