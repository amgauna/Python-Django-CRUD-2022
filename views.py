from django.http import HttpResponse
from django.shortcuts import render
from app.forms import CarrosForm
from app.models import Carros
from django.contrib import admin
from django.urls import path
from app.views import delete


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

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


<div class="col-8 m-auto pt-2 pb-2 text-center">
    <h1>Visualização</h1>
</div>

<div class="col-8 m-auto pt-3 pb-2 text-center">
    <a href="/" class="btn btn-info">Voltar</a>
</div>

<div class="col-8 m-auto pt-4 pb-2 text-center">
    <strong>Modelo: </strong>{{db.modelo}}<br>
    <strong>Marca: </strong>{{db.marca}}<br>
    <strong>Ano: </strong>{{db.ano}}<br>
</div>

# Apagar dados no Python com Ajax
# Vamos criar a url que será responsável por eliminar os dados no nosso banco:

urlpatterns = [
    path('delete/<int:pk>/', delete, name='delete'),
]

# Já vamos criar a função view relativa ao delete:

def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')

# Vamos chamar o módulo paginator para facilitar o nosso trabalho com a separação dos dados em páginas:
def home(request):
    data = {}
    all = Carros.objects.all()
    paginator = Paginator(all, 2)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

# Para implementar a busca na views:
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carros.objects.all()
    return render(request, 'index.html', data)

