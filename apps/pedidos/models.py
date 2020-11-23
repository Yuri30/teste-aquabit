from django.db import models
from apps.clientes.models import Cliente
from apps.Produtos.models import Produto, Pratos

# Create your models here.

class Pedido(models.Model):
    EM ABERTO = 1
    ENCERRADO = 2
    SITUACOES = (
        (EM ABERTO, 'Pendente'),
        (ENCERRADO, 'Cancelado'),
    )


    class Meta:
        db_table = 'pedido'


    cliente = models.ManyToManyField(Cliente)
    data = models.DateField(auto_now_add=False)
    pago = models.BooleanField(defaut=False)
    situacao = models.IntegerField(choices=SITUACOES, default=EM ABERTO)
    observação = models.TextField(max_length = 500)
    valor_total = models.FloatField()
    produto = models.ForignKey(Porduto, on_delete=models.CASCADE)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pratos = models.ForeignKey(Pratos, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'Item do {self.pedido}'    

    
    