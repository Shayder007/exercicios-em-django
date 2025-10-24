from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^numero/(?P<num>\d{1,5})/$', views.mostra_numero, name='mostra_numero'),
]