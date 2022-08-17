from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.contrib import auth, messages
from receitas.models import Receita

def busca (request):
    """Executa função de busca de receitas"""
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'search' in request.GET:
        nome_a_buscar = request.GET['search']
        if nome_a_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas' : lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)