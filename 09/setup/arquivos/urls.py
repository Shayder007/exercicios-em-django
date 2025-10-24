from django.urls import path
from . import views

urlpatterns = [
    path('download/<str:nome>.<str:ext>/', views.download, name='download'),
]