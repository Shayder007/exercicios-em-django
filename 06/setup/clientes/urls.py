from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='clientes_index'),
    path('detalhes/<int:id>/', views.detalhes, name='clientes_detalhes'),
]