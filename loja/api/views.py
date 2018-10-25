from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PedidoSerializer
from .serializers import ProdutoSerializer
from .serializers import CategoriaSerializer

from .models import Produto, Categoria, Pedido


class ProdutoView(ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriaView(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class PedidoView(APIView):
    serializer_class = PedidoSerializer

    def get(self, request, format=None):
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        dados = self.soma_preco_produto(request)
        dados['status'] = dados['status'][0]

        serializer = PedidoSerializer(data=dados)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def soma_preco_produto(self, request):
        lista_preco_produto = []
        dados = dict(request.data.lists())

        for id in dados['produto']:
            produto = Produto.objects.get(id=id)
            lista_preco_produto.append(produto.preco)

        dados['preco'] = sum(lista_preco_produto)

        return dados