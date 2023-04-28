import mysql.connector
from item_pedido import ItemPedido
from pedido import Pedido
from cliente import Cliente
from pizza import Pizza
from lanche import Lanche
from salgado import Salgado
from typing import Any

#from prato import Prato

class Repositorio:
    def __init__(self):
       self._cursor: Any = None

    @property
    def cursor(self):
        if self._cursor is None:
            cnx = mysql.connector.connect(user='dono_lanchonete',
                                          password='uma_senha_forte',
                                          host='localhost',
                                          database='lanchonete')
            print('Conexão estabelecida com Banco de Dados')
            # Cria um cursor para executar consultas
            self._cursor = cnx.cursor()

        return self._cursor

    def lanches(self):
        #Busca todos os dados de pratos que sao lanches
        query_lanches = """
            SELECT lanche.id_prato, nome_prato, preco, validade, peso, pao, recheio, molhos 
            FROM lanche
            JOIN prato ON lanche.id_prato = prato.id_prato"""
        self.cursor.execute(query_lanches)

        # Mapeia os dados do banco de dados para a classe Lanche
        lanches = [Lanche(id_prato, nome_prato, preco, validade, peso, pao, recheio, molho)
                   for (id_prato, nome_prato, preco, validade, peso, pao, recheio, molho)
                   in self.cursor]
        print(f'Lanches:', [str(lanche) for lanche in lanches])

    def pizzas(self):
        query_pizzas = """
            SELECT pizza.id_prato, nome_prato, preco, validade, peso, molho, recheio, borda
            FROM pizza
            JOIN prato
                ON pizza.id_prato = prato.id_prato            
        """
        self.cursor.execute(query_pizzas)
        pizzas = [Pizza(id_prato, nome_prato, preco, validade, peso, molho, recheio, borda)
                   for (id_prato, nome_prato, preco, validade, peso, molho, recheio, borda)
                   in self.cursor]
        print(f'Pizzas:', [str(pizza) for pizza in pizzas])


    def salgados(self):
        query_salgados = """
            SELECT salgado.id_prato, nome_prato, preco, validade, peso, recheio, massa
            FROM salgado
            JOIN prato
                ON salgado.id_prato = prato.id_prato;            
        """
        self.cursor.execute(query_salgados)
        salgados = [Salgado(id_prato, nome_prato, preco, validade, peso, recheio, massa)
                   for (id_prato, nome_prato, preco, validade, peso, recheio, massa)
                   in self.cursor]
        print(f'Salgados:', [str(salgado) for salgado in salgados])

    def clientes(self):
        query_clientes = """
            SELECT cliente.id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos
            FROM cliente;          
        """
        self.cursor.execute(query_clientes)
        clientes = [Cliente(id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos)
                   for (id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos)
                   in self.cursor]
        print(f'Clientes:', [str(cliente) for cliente in clientes])

    def itens_pedido(self):
        query_item_pedido = """
            SELECT  id_item, id_pedido, id_prato, quantidade
            FROM item_pedido;          
        """
        self.cursor.execute(query_item_pedido)
        itens_pedido = [ItemPedido(id_item, id_pedido, id_prato, quantidade)
                       for (id_item, id_pedido, id_prato, quantidade)
                       in self.cursor]
        print(f'Itens pedido:', [str(item_pedido) for item_pedido in itens_pedido])

    def pedidos(self):
        query_pedido = """
            SELECT
            pedido.id_pedido,
            cliente.id_cliente,
            item_pedido.id_item,
            pedido.taxa_servico,
            pedido.status
            FROM pedido
            JOIN item_pedido ON pedido.id_pedido = item_pedido.id_prato
            JOIN prato ON item_pedido.id_prato = prato.id_prato
            JOIN cliente ON pedido.id_cliente = cliente.id_cliente;         
            """
        self.cursor.execute(query_pedido)
        pedidos = [Pedido(id_pedido, id_cliente, itens_pedido, taxa_servico, status)
                   for (id_pedido, id_cliente, itens_pedido, taxa_servico, status,)
                   in self.cursor]

        print(f'Pedidos:', [str(pedido) for pedido in pedidos])

