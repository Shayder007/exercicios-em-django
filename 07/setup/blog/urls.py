from django.urls import path
from . import views

urlpatterns = [
    # /artigo/<slug>/
    path('<slug:slug>/', views.artigo, name='artigo'),
]