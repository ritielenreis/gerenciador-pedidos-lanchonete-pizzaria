from pedido import Pedido
from cliente import Cliente
from pizza import Pizza
from lanche import Lanche
from salgado import Salgado
from repositorio import Repositorio
from repositorio_atual import RepositorioAtual
from cardapio import *
repositorio = Repositorio
cardapio()

repositorio_atual = RepositorioAtual()
repositorio_atual.itens_pedido_atual(1)

