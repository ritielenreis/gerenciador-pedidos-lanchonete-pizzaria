from pedido import Pedido
from cliente import Cliente
from pizza import Pizza
from lanche import Lanche
from salgado import Salgado
from repositorio import Repositorio
from repositorio_atual import RepositorioAtual
from cardapio import *


repositorio_atual = RepositorioAtual()
repositorio_atual.itens_pedido_atual(1)
repositorio_atual.calculo_preco_itens(1)
repositorio_atual.calculo_taxa(1)