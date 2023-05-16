from mysql.connector import connect, Error
from item_pedido import ItemPedido
from pedido import Pedido
from cliente import Cliente
from pizza import Pizza
from lanche import Lanche
from salgado import Salgado
from typing import Any

#from prato import Prato


class RepositorioAtual:
    def __init__(self):
        self.connection = connect(user='dono_lanchonete',
                         password='uma_senha_forte',
                         host='localhost',
                         database='lanchonete')

    def _executar_query(self, query):
        try:
            with self.connection:
                print('Conexão estabelecida com Banco de Dados')
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
        except Error as e:
            print(e)


    def _retornar_resultado(self, query):
        try:
            print('Conexão estabelecida com Banco de Dados')
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchone()
        except Error as e:
            print(e)

    def _retornar_resultados(self, query):
        try:
            print('Conexão estabelecida com Banco de Dados')
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(e)

    def itens_pedido_atual(self, id_pedido):
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
            item_pedido = ItemPedido(id_pedido, id_item,  id_prato, nome_prato, quantidade, preco, validade, peso)
            itens_pedido.append(item_pedido)
        print(itens_pedido)
        return itens_pedido


    def item_pedido_atual(self, id_pedido_atual):
        query_itens_pedido = f'SELECT * FROM item_pedido WHERE id_pedido = {id_pedido_atual}'
        resultados = self._retornar_resultado(query_itens_pedido)
        itens_pedido_atual = [ItemPedido(id_item, id_pedido, id_prato, quantidade)
                        for (id_item, id_pedido, id_prato, quantidade)
                        in resultados]
        print([str(item_pedido) for item_pedido in itens_pedido_atual])
        return itens_pedido_atual
