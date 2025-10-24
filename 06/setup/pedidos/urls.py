from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pedidos_index'),
    path('detalhes/<int:id>/', views.detalhes, name='pedidos_detalhes'),
]