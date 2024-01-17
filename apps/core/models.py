from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    foto = models.ImageField(upload_to='fotos/',null=True,blank=True)
    cpf = models.CharField(max_length=11,unique=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    celular = models.CharField(max_length=11)
    
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="usuarios_groups"  # Adicione o related_name aqui
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="usuarios_user_permissions"  # Adicione o related_name aqui
    )
    
    class Meta:
        app_label = 'core'

class Prestador(models.Model):
    usuario_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usuario_prestador')
    portfolio = models.CharField(max_length=255)
    ramo = models.CharField(max_length=255)
    especialidade = models.CharField(max_length=255,null=True)
    local_max = models.IntegerField(null=True)
    num_servicos = models.IntegerField()
    num_solicitacoes = models.IntegerField()

class Cliente(models.Model):
    usuario_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usuario_cliente')
    num_servicos = models.IntegerField()
    num_solicitacoes = models.IntegerField()

class Review(models.Model):
    avaliador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='avaliador_reviews')
    avaliado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='avaliado_reviews')
    conteudo = models.TextField()
    pontuacao = models.IntegerField()
    data_hora = models.DateTimeField()

class Chat(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente_chats')
    prestador_id = models.ForeignKey(Prestador, on_delete=models.CASCADE, related_name='prestador_chats')
    mensagens = models.TextField()
    data_hora = models.DateTimeField()

class Pagamento(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pagamento_cliente')
    prestador_id = models.ForeignKey(Prestador, on_delete=models.CASCADE, related_name='pagamento_prestador')
    servico_id = models.OneToOneField('Servico', on_delete=models.CASCADE, related_name='pagamento')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField()
    metodo = models.CharField(max_length=255)

class Carteira(models.Model):
    prestador_id = models.OneToOneField(Prestador, on_delete=models.CASCADE)
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
    local = models.CharField(max_length=255,null=True)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=255)

class Solicitacao(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='solicitacao_cliente')
    prestador_id = models.ForeignKey(Prestador, on_delete=models.CASCADE, related_name='solicitacao_prestador')
    servico_id = models.OneToOneField(Servico, on_delete=models.CASCADE, related_name='solicitacao_servico')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    local = models.CharField(max_length=255,null=True)
    data_hora_solicitacao = models.DateTimeField()
    data_hora_servico = models.DateTimeField()
    status = models.CharField(max_length=255)