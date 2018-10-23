from rest_framework.generics import ListCreateAPIView
from .serializers import ProdutoSerializer, CategoriaSerializer
from .models import Produto, Categoria


class ProdutoView(ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriaView(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
