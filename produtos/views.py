from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy

from produtos.forms import CategoriaForm, ProdutoForm
from produtos.models import Categoria, Produto


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/categoria_list.html'


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria_update')
    
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_delete')



# --------------------------------------------------------------------------



class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/produto_list.html'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/produto_form.html'
    success_url = reverse_lazy('produto_create')

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/produto_form.html'
    success_url = reverse_lazy('produto_update')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_delete')