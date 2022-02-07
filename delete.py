# Apagar dados no Python com Ajax
# Vamos criar a url que será responsável por eliminar os dados no nosso banco:

from django.contrib import admin
from django.urls import path
from app.views import delete

urlpatterns = [
    path('delete/<int:pk>/', delete, name='delete'),
]
