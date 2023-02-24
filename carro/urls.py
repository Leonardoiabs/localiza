from django.urls import path, include
from carro.view import *


urlpatterns = [
    # minhas rotas
    path('', HomeCarro.as_view(), name="home_carro"),

]
