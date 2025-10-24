from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index, name='blog_index'),
    path('blog/post/<int:ano>/<slug:slug>/', views.post, name='blog_post'),
    path('blog/autor/<str:nome>/', views.autor, name='blog_autor'),
]