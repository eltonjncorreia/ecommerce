from django.urls import path
from .views import ProdutoView, ProdutoDetailView
from .views import CategoriaView
from .views import PedidoView

urlpatterns = [
    path('v1/produtos/', ProdutoView.as_view(), name="produtos"),
    path('v1/produtos/<uuid:pk>/', ProdutoDetailView.as_view(), name="produtos-detail"),
    path('v1/categorias/', CategoriaView.as_view(), name="categorias"),
    path('v1/pedidos/', PedidoView.as_view(), name="pedidos"),

]
