from django.urls import path
from . import views

urlpatterns = [
    path('categoria/<str:categoria>/produto/<str:produto>/', views.produto, name='produto'),
]