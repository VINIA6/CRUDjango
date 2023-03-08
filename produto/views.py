from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from produto.models import Produto

# As views criam funções que gerenciam os atributos no banco de dados CRUD 

class ProdutoNovo(generic.CreateView):
    # Criar produto no BD.
    model = Produto
    fields = '__all__'

class ProdutoDetalhe(generic.DetailView):
    #Buscar informações no BD 
    model = Produto

class ProdutoLista(generic.ListView):
    model = Produto
    #Retorna os dados do BD
    queryset = model.objects.all()

class ProdutoAtualizar(generic.UpdateView):
    model = Produto
    #Atualiza informações no BD
    fields = ['nome','preco',]  
    template_name_sulfix='_update_form'

class ProdutoDeletar(generic.DeleteView):
    #Deletar informações do BD
    model= Produto
    success_url = reverse_lazy('produto-lista')

