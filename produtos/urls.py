from django.urls import path
from .views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView,ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('categoria/', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/novo/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/<int:pk>/edit/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/<int:pk>/delete/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('produtos/', ProdutoListView.as_view(), name='produto_list'),
    path('produtos/novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/edit/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/delete/', ProdutoDeleteView.as_view(), name='produto_delete'),
]

