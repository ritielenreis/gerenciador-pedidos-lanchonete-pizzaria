from mysql.connector import connect, Error
from item_pedido import ItemPedido
from info_item_pedido import InfoItemPedido
from cliente import Cliente
from pedido_info import PedidoInfo
from typing import List


class RepositorioAtual:
    def __init__(self):
        self.connection = \
            connect(user='dono_lanchonete', password='uma_senha_forte', host='localhost', database='lanchonete')

    def _executar_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
        except Error as e:
            self.connection.rollback()
            print(f"[{self.__class__.__name__}] Error:", e)

    def _retornar_resultado(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchone()
        except Error as e:
            print(f"[{self.__class__.__name__}] Error:", e)

    def _retornar_resultados(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"[{self.__class__.__name__}] Error:", e)

    def itens_pedido_atual(self, id_pedido) -> List[InfoItemPedido]:
        query_item_pedido = f"""
            SELECT  item_pedido.id_pedido, item_pedido.id_item,  item_pedido.id_prato,
            prato.nome_prato, item_pedido.quantidade,  prato.preco, prato.validade, prato.peso
            FROM item_pedido
            JOIN pedido ON item_pedido.id_pedido = pedido.id_pedido
            JOIN prato ON item_pedido.id_prato = prato.id_prato
            WHERE item_pedido.id_pedido = {id_pedido};          
        """
        resultados = self._retornar_resultados(query_item_pedido)
        itens_pedido = []
        for (id_pedido, id_item,  id_prato, nome_prato, quantidade, preco, validade, peso) in resultados:
            item_pedido = InfoItemPedido(id_pedido, id_item,  id_prato, nome_prato, quantidade, preco, validade, peso)
            itens_pedido.append(item_pedido)
        return itens_pedido


    def pedido_atual(self, id_pedido):
        query_pedido_atual = f"""
            SELECT pedido.id_cliente, cliente.nome_cliente, pedido.id_pedido, pedido.status
            FROM pedido
            JOIN cliente ON pedido.id_cliente = cliente.id_cliente
            WHERE pedido.id_pedido = {id_pedido};          
        """
        resultados = self._retornar_resultados(query_pedido_atual)
        list_pedido_atual = ''
        for (id_cliente, nome_cliente, id_pedido, status) in resultados:
            pedido = PedidoInfo(id_cliente, nome_cliente, id_pedido, status)
            list_pedido_atual = pedido
        return list_pedido_atual

    def info_cliente(self, id_cliente):
        query_info_cliente = f"SELECT * FROM cliente WHERE id_cliente = {id_cliente};"
        resultado = self._retornar_resultado(query_info_cliente)
        info_cliente = ''
        for (id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos) in resultado:
            cliente = Cliente(id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos)
            info_cliente = cliente
        return info_cliente

    def info_item(self, id_pedido, id_item):
        query_info_item = f"SELECT * FROM item_pedido WHERE id_pedido = {id_pedido} and id_item = {id_item};;"
        resultado = self._retornar_resultado(query_info_item)
        info_item = ''
        for (id_pedido, id_item,  id_prato, quantidade) in resultado:
            item = ItemPedido(id_pedido, id_item,  id_prato, quantidade)
            info_item = item
        return info_item
