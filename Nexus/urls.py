"""
URL configuration for Nexus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import (
    UsuarioViewSet, PrestadorViewSet, ClienteViewSet, ReviewViewSet, ChatViewSet,
    CarteiraViewSet, ExtratoViewSet, PagamentoViewSet, SolicitacaoViewSet, ServicoViewSet
)

router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'prestadores', PrestadorViewSet, basename='prestador')
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'chats', ChatViewSet, basename='chat')
router.register(r'carteiras', CarteiraViewSet, basename='carteira')
router.register(r'extratos', ExtratoViewSet, basename='extrato')
router.register(r'pagamentos', PagamentoViewSet, basename='pagamento')
router.register(r'solicitacoes', SolicitacaoViewSet, basename='solicitacao')
router.register(r'servicos', ServicoViewSet, basename='servico')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
