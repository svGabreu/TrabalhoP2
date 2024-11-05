from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = 'todos/produto_list.html'
    context_object_name = 'produto_list'  # Certifique-se de que o nome do contexto está correto

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome','descricao','preco','categoria']
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome','descricao','preco','categoria']
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy('produto_list')