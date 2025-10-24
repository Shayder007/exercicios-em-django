from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^produto/(?P<nome>[A-Za-z\-]+)/$', views.produto, name='produto'),
]