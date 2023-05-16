from item_pedido import ItemPedido
from pedido import Pedido
from cliente import Cliente
from pizza import Pizza
from lanche import Lanche
from salgado import Salgado
from prato import Prato
from repositorio import Repositorio



class Calculo:
    #print('Preço por item_pedido, Total, Nota fiscal, Troco.')
    def __init__(self):
        self._repositorio = Repositorio()

    def preco_item_pedido(self, id_pedido_atual):
        return str(self._repositorio.itens_pedido_atual(id_pedido_atual))

calculo = Calculo()
calculo.preco_item_pedido(15)

