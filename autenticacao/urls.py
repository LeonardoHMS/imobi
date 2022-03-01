from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="Cadastro"),
    path('logar/', views.logar, name="Logar"),
    path('sair/', views.sair, name="sair")  
]    