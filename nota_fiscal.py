from tabulate import tabulate
from item_pedido import ItemPedido
from typing import List
from calculo import Calculo


class NotaFiscal:
    def __init__(self, repositorio_atual):
        self.repositorio_atual = repositorio_atual

    def ver_info_pedido(self, id_pedido):
        calculo = Calculo(self.repositorio_atual)
        pedido = self.repositorio_atual.pedido_atual(id_pedido)
        itens_pedido: List[ItemPedido] = self.repositorio_atual.itens_pedido_atual(id_pedido)
        taxa_servico = calculo.calculo_taxa(id_pedido)
        total_geral = calculo.calculo_preco_itens(id_pedido) + taxa_servico

        print('=' * 36, 'FATURA', '=' * 36, '\nPedido n°:', pedido.id_pedido, '\nCliente:', pedido.nome_cliente)
        table_itens_pedido = [[id_pedido, '0', 'Taxa de Serviço', '1', taxa_servico]]
        for item in itens_pedido:
            table_itens_pedido.append([item.id_pedido, item.id_prato, item.nome_prato, item.quantidade, item.preco])
        print(tabulate(table_itens_pedido, headers=('Id_pedido', 'Id_prato', 'Nome_prato', 'Qtd', 'Preco')))
        print(f'\033[7:32:49mTotal do Pedido:        {total_geral:>55}\033[0m')
        return float(total_geral)

    def pagamento(self, id_pedido):
        total_geral = self.ver_info_pedido(id_pedido)
        valor_pago = float(input('Valor pago: '))
        troco = valor_pago - total_geral
        table_calculos = [['Total a Pagar', f'{total_geral:>55}'], ['Valor Pago', f'{valor_pago:>55}']]
        if troco > 0:
            table_calculos.append(['\033[7:32:49mTroco', f'{troco:>55}\033[0m'])
        elif troco < 0:
            troco = troco * -1
            table_calculos.append(['\033[7:31:49m Falta pagar', f'{troco:>55}\033[0m'])
        print(tabulate(table_calculos))
