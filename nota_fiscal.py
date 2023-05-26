from mysql.connector import connect, Error
from tabulate import tabulate
from item_pedido import ItemPedido
from pedido import Pedido
from cliente import Cliente
from pizza import Pizza
from lanche import Lanche
from salgado import Salgado
from typing import Any, List
from prato import Prato
from calculo import Calculo


class NotaFiscal:
    def __init__(self, repositorio_atual):
        self.repositorio_atual = repositorio_atual

    def emitir_nota(self, id_pedido):
        calculo = Calculo(self.repositorio_atual)
        pedido = self.repositorio_atual.pedido_atual(id_pedido)
        itens_pedido: List[ItemPedido] = self.repositorio_atual.itens_pedido_atual(id_pedido)
        taxa_servico = calculo.calculo_taxa(id_pedido)
        total_geral = calculo.calculo_preco_itens(id_pedido) + taxa_servico

        print('=' * 10, 'Fatura', '=' * 10, '\nPedido n°:', pedido.id_pedido, '\nCliente:', pedido.nome_cliente)
        table_itens_pedido = [[id_pedido, '0', 'Taxa de Serviço', '1', taxa_servico]]
        for item in itens_pedido:
            table_itens_pedido.append([item.id_pedido, item.id_prato, item.nome_prato, item.quantidade, item.preco])
        print(tabulate(table_itens_pedido, headers=('Id_pedido', 'Id_prato', 'Nome_prato', 'Qtd', 'Preco')))

        valor_pago = 300
        troco = valor_pago - total_geral

        table_calculos = [['Total a Pagar', total_geral], ['Valor Pago', valor_pago], ['Troco', troco]]

        print(tabulate(table_calculos))

