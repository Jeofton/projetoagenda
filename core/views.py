from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from .models import Contato


def index(request):
    
    contatos = Contato.objects.order_by('-data_criacao').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 2)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'core/index.html', {'contatos': contatos})


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404()
    return render(request, 'core/ver_contato.html', {'contato': contato})

def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Campo de pesquisa não pode ficar vazio.')
        return redirect(index)

    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(nome_completo=campos).filter(Q(nome_completo__icontains=termo)| Q(telefone__icontains=termo)
    )
    paginator = Paginator(contatos, 2)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'core/busca.html', {'contatos': contatos})
    