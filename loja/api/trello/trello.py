import json
from uuid import UUID

from trello import TrelloClient

from loja.api.models import Produto
from loja.settings import API_KEY, API_TOKEN


def cartao_trello(request, pedido=None, descricao=None):
    """Responsavel por enviar ao cartao trello."""
    cliente = TrelloClient(api_key=API_KEY, api_secret=API_TOKEN)
    my_boards = cliente.get_board('6CMTUQRG')
    lista = my_boards.all_lists()

    for id in descricao:
        produto = Produto.objects.get(id=id)
        descricao = f"{produto.nome}, {produto.descricao}, {produto.preco}"

    pedido = json.dumps(pedido, cls=UUIDEncoder)
    desc = json.dumps(descricao, cls=UUIDEncoder)
    lista[0].add_card(name="Pedido "+pedido, desc=desc, position=0)



class UUIDEncoder(json.JSONEncoder):
    """Class encode UUID."""

    def default(self, obj):
        """Usando para enviar UUID."""
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)