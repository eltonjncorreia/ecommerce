from django.urls import path
from .views import ProdutoView, ProdutoDetailView, CategoriaView

urlpatterns = [
    path('v1/produtos/', ProdutoView.as_view(), name="produtos"),
    path('v1/produtos/<uuid:pk>/', ProdutoDetailView.as_view(), name="produtos-detail"),
    path('v1/categorias/', CategoriaView.as_view(), name="categorias"),

]
