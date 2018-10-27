from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE,
                                  related_name='categoria_do_produto')

    def __str__(self):
        return f'{self.nome}, {self.descricao}'


class Pedido(models.Model):
    STATUS = (('PR', 'Pedido Realizado'),
              ('SP', 'Separação em estoque'),
              ('EM', 'Em montagem'),
              ('RT', 'Realização de testes'),
              ('CO', 'Concluido'))

    produto = models.ManyToManyField('Produto', related_name='produtos_em_pedidos')
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    status = models.CharField(max_length=2, choices=STATUS, default='PR')

    def __str__(self):
        return f'{self.produto}'


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome}'


class Estoque(models.Model):
    item = models.ForeignKey('Produto', on_delete=models.CASCADE, related_name='produto_em_estoque')
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.item}, {self.quantidade}'
