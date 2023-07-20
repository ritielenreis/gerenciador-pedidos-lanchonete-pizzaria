from tabulate import tabulate
from objetos.info_item_pedido import InfoItemPedido
from typing import List
from calculo import Calculo
from repositorios import (
    RepositorioAdm,
    RepositorioCliente,
    RepositorioPrato,
    RepositorioPizza,
    RepositorioSalgado,
    RepositorioLanche,
    RepositorioPedido,
    RepositorioItemPedido
)


class NotaFiscal:
    def __init__(self):
        self._repositorio_cliente = RepositorioCliente()
        self._repositorio_adm = RepositorioAdm()
        self._repositorio_pizza = RepositorioPizza()
        self._repositorio_lanche = RepositorioLanche()
        self._repositorio_salgado = RepositorioSalgado()
        self._repositorio_prato = RepositorioPrato()
        self._repositorio_pedido = RepositorioPedido()
        self._repositorio_item_pedido = RepositorioItemPedido()

    def ver_info_pedido(self, id_pedido):
        calculo = Calculo()
        pedido = self._repositorio_pedido.ler_pedido(id_pedido)
        itens_pedido: List[InfoItemPedido] = self._repositorio_item_pedido.ler_info_itens_pedido(id_pedido)
        taxa_servico = calculo.calculo_taxa(id_pedido)
        total_geral = calculo.calculo_preco_itens(id_pedido) + taxa_servico

        print('=' * 36, 'FATURA', '=' * 36, '\nPedido n°:', pedido.id_pedido, '\nCliente:', pedido.nome_cliente)
        table_itens_pedido = [['0', 'Taxa de Serviço', '1', taxa_servico]]
        for item in itens_pedido:
            table_itens_pedido.append([item.id_prato, item.nome_prato, item.quantidade, item.preco])
        print(tabulate(table_itens_pedido, headers=('Id_prato', 'Nome_prato', 'Qtd', 'Preco')))
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
