from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('retorna_total_vendido', views.retorna_total_vendido, name='retorna_total_vendido'),
    path('relatorio_faturamento', views.relatorio_faturamento, name='relatorio_faturamento'),
    path('relatorio_produtos', views.relatorio_produtos, name='relatorio_produtos'),
    path('relatorio_funcionario', views.relatorio_funcionario, name='relatorio_funcionario'),
    path('retorna_total_despesa', views.retorna_total_despesa, name='retorna_total_despesa'),
    path('retorna_total_lucro', views.retorna_total_lucro, name='retorna_total_lucro'),
    path('relatorio_despesa', views.relatorio_despesa, name='relatorio_despesa')
    
]