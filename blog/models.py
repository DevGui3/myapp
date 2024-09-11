from django.db import models


class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return sel.nome


class Stock(models.Model):
    quantity = models.DecimalField(max_digits=10)