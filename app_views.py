from django.http import HttpResponse
from django.shortcuts import render

def form(request):
    return render(request, 'form.html')

# Create your views here.
def home(request):
    return HttpResponse('Hello World')

# Create your views here.
def home(request):
    return render(request, 'index.html')

# Podemos também passar comandos de dados vindos do backend para o 
# frontend utilizando {%%} e impressões literais usando {{}}

{% if carro == 'Fiat Uno' %}
    Esse é um carro {{carro}}
{% else %}
    Não tem carro
{% endif %}
