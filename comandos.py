from repositorio import Repositorio
from repositorio_atual import RepositorioAtual
from cardapio import *
from nota_fiscal import NotaFiscal
from calculo import Calculo


repositorio_atual = RepositorioAtual()
nota_fiscal = NotaFiscal(repositorio_atual)
calculo = Calculo(repositorio_atual)
###Ver itens do pedido desejado
#repositorio_atual.itens_pedido_atual(1)

###Calcular o preço total dos itens do pedido desejado
#repositorio_atual.calculo_preco_itens(1)

###Calcular o valor da taxa de serviço do pedido desejado
#repositorio_atual.calculo_taxa(1)
repositorio_atual.pedido_atual(1)
nota_fiscal.emitir_nota(1)

