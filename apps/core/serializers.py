from rest_framework import serializers
from .models import Usuario, Prestador, Cliente, Review, Chat, Carteira, Extrato, Pagamento, Solicitacao, Servico

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'foto', 'cpf', 'password', 'bairro', 'cidade', 'estado', 'celular']
        extra_kwargs = {'password': {'write_only': True}}
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['foto']:
            # Se o campo foto for nulo, use a URL da imagem padrão
            data['foto'] = '/static/img/padrao.jpg'  # Substitua com o caminho real
        return data

class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestador
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class CarteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carteira
        fields = '__all__'

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = '__all__'

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'

class SolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'