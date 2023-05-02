from django.db import models

# Create your models here.

from datetime import date


class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length= 50)
    co_autor = models.CharField(max_length= 50, null=True, blank=True)
    data_cadastro = models.DateField(default = date.today)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=50, null=True, blank=True)
    data_emprestimo = models.DateTimeField(null=True,blank=True)
    data_devolucao = models.DateTimeField(null=True,blank=True)
    duracao = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Livro';

    def __str__(self):
        return self.nome