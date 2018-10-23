from rest_framework.views import APIView
from .serializers import ProdutoSerializer
from .models import Produto


class ProdutoViewSet(APIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    @classmethod
    def get(cls, request):
        url = 'https://api.github.com/users'
        response = requests.get(url)
        usuarios = response.json()
        serializer = UserGithubSerializer(usuarios, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

