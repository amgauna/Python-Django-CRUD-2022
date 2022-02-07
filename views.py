from django.shortcuts import render
from app.forms import CarrosForm
from app.models import Carros

# Create your views here.
def home(request):
    return render(request, 'index.html')

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

