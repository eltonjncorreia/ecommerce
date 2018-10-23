from django.urls import path
from .views import ProdutoView, CategoriaView

urlpatterns = [
    path('v1/produtos/', ProdutoView.as_view(), name="produtos"),
    path('v1/categorias/', CategoriaView.as_view(), name="categorias"),

]
