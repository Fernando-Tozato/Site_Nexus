# No arquivo admin.py

from django.contrib import admin
from .models import Prestador, Cliente, Review, Chat, Pagamento, Carteira, Extrato, Servico, Solicitacao  # Importe os modelos necessários

admin.site.register(Prestador)
admin.site.register(Cliente)
admin.site.register(Review)
admin.site.register(Chat)
admin.site.register(Pagamento)
admin.site.register(Carteira)
admin.site.register(Extrato)
admin.site.register(Servico)
admin.site.register(Solicitacao)