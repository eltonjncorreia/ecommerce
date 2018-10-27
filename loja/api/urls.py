from django.urls import path
from .views import ProdutoView, ProdutoDetailView
from .views import CategoriaView
from .views import PedidoView, PedidoDetailView

app_name = 'api_name'

urlpatterns = [
    path('v1/produtos/', ProdutoView.as_view(), name="produtos"),
    path('v1/produtos/<int:pk>/', ProdutoDetailView.as_view(), name="produto-detail"),
    path('v1/categorias/', CategoriaView.as_view(), name="categorias"),
    path('v1/pedidos/', PedidoView.as_view(), name="pedidos"),
    path('v1/pedidos/<int:pk>/', PedidoDetailView.as_view(), name="pedido-detail"),

]
