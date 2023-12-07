from django.db import models
from django.contrib.auth.models import User

class Prestador(models.Model):
    usuario_id = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.CharField(max_length=255)
    ramo = models.CharField(max_length=255)
    num_servicos = models.IntegerField()
    num_solicitacoes = models.IntegerField()

class Cliente(models.Model):
    usuario_id = models.OneToOneField(User, on_delete=models.CASCADE)
    num_servicos = models.IntegerField()
    num_solicitacoes = models.IntegerField()

class Review(models.Model):
    avaliador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avaliador_reviews')
    avaliado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avaliado_reviews')
    conteudo = models.TextField()
    pontuacao = models.IntegerField()
    data_hora = models.DateTimeField()

class Chat(models.Model):
    cliente_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cliente_chats')
    prestador_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prestador_chats')
    mensagens = models.TextField()
    data_hora = models.DateTimeField()

class Pagamento(models.Model):
    cliente_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pagamento_cliente')
    prestador_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pagamento_prestador')
    servico_id = models.OneToOneField('Servico', on_delete=models.CASCADE, related_name='pagamento')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField()
    metodo = models.CharField(max_length=255)

class Carteira(models.Model):
    prestador_id = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_disponivel = models.DecimalField(max_digits=10, decimal_places=2)

class Extrato(models.Model):
    carteira_id = models.ForeignKey(Carteira, on_delete=models.CASCADE, related_name='extratos')
    data_hora = models.DateTimeField()
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Servico(models.Model):
    solicitacao_id = models.OneToOneField('Solicitacao', on_delete=models.CASCADE, related_name='servico')
    pagamento_id = models.OneToOneField(Pagamento, on_delete=models.CASCADE, related_name='servico_pagamento')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=255)

class Solicitacao(models.Model):
    cliente_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacao_cliente')
    prestador_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacao_prestador')
    servico_id = models.OneToOneField(Servico, on_delete=models.CASCADE, related_name='solicitacao_servico')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora_solicitacao = models.DateTimeField()
    data_hora_servico = models.DateTimeField()
    status = models.CharField(max_length=255)