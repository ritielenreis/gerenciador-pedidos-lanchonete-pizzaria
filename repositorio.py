from mysql.connector import connect, Error
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

    def _retornar_resultados(self, query):
        try:
            print('Conexão estabelecida com Banco de Dados')
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
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

    def lanches(self):
        #Busca todos os dados de pratos que são lanches
        query_lanches = """
            SELECT lanche.id_prato, nome_prato, preco, validade, peso, pao, recheio, molhos 
            FROM lanche
            JOIN prato ON lanche.id_prato = prato.id_prato"""
        resultados = self._retornar_resultados(query_lanches)

        # Transformar os resultados em objetos
        lanches = []
        for (id_prato, nome_prato, preco, validade, peso, pao, recheio, molho) in resultados:
            lanche = Lanche(id_prato, nome_prato, preco, validade, peso, pao, recheio, molho)
            lanches.append(lanche)
        return lanches
        # Mostrar os objetos criados

    def pizzas(self):
        query_pizzas = """
            SELECT pizza.id_prato, nome_prato, preco, validade, peso, molho, recheio, borda
            FROM pizza
            JOIN prato
                ON pizza.id_prato = prato.id_prato            
        """
        resultados = self._retornar_resultados(query_pizzas)
        # Transformar os resultados em objetos
        pizzas = []
        for (id_prato, nome_prato, preco, validade, peso, molho, recheio, borda) in resultados:
            pizza = Pizza(id_prato, nome_prato, preco, validade, peso, molho, recheio, borda)
            pizzas.append(pizza)
        return pizzas

    def salgados(self):
        query_salgados = """
            SELECT salgado.id_prato, nome_prato, preco, validade, peso, recheio, massa, tipo_salgado
            FROM salgado
            JOIN prato
                ON salgado.id_prato = prato.id_prato;            
        """
        resultados = self._retornar_resultados(query_salgados)
        salgados = []
        for (id_prato, nome_prato, preco, validade, peso, recheio, massa, tipo_salgado) in resultados:
            salgado = Salgado(id_prato, nome_prato, preco, validade, peso, recheio, massa, tipo_salgado)
            salgados.append(salgado)
        return salgados

    def clientes(self) -> list[Cliente]:
        query_clientes = """
            SELECT cliente.id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos
            FROM cliente;          
        """
        resultados = self._retornar_resultados(query_clientes)
        clientes = []
        for (id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos) in resultados:
            cliente = Cliente(id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos)
            clientes.append(cliente)
        return clientes

    def itens_pedido(self):
        query_item_pedido = """
            SELECT  id_item, id_pedido, id_prato, quantidade
            FROM item_pedido;          
        """
        resultados = self._retornar_resultados(query_item_pedido)
        itens_pedido = [ItemPedido(id_item, id_pedido, id_prato, quantidade)
                        for (id_item, id_pedido, id_prato, quantidade)
                        in resultados]
        print(f'Itens pedido:', [str(item_pedido) for item_pedido in itens_pedido])
        return itens_pedido

    def criar_pedido(self, id_cliente: int) -> Pedido:
        query = f"""
            INSERT INTO pedido (id_cliente) VALUES({id_cliente})
            """
        self._executar_query(query)
        query = f"""
            SELECT LAST_INSERT_ID(id_pedido) from pedido
            """
        pedido = self._retornar_resultados(query)
        return Pedido()

    def pedido_por(self, id_pedido):
        query_pedido = f"""
            SELECT
            pedido.id_pedido,
            cliente.id_cliente,
            item_pedido.id_item,
            pedido.taxa_servico,
            pedido.status
            FROM pedido
            JOIN item_pedido ON pedido.id_pedido = item_pedido.id_prato
            JOIN prato ON item_pedido.id_prato = prato.id_prato
            JOIN cliente ON pedido.id_cliente = cliente.id_cliente
            WHERE pedido.id_pedido = {id_pedido};         
            """
        resultados = self._retornar_resultados(query_pedido)
        pedidos = [Pedido(id_pedido, id_cliente, itens_pedido, taxa_servico, status)
                   for (id_pedido, id_cliente, itens_pedido, taxa_servico, status)
                   in resultados]

        print(f'Pedidos:', [str(pedido) for pedido in pedidos])
        return pedidos

    def itens_pedido_atual(self, id_pedido_atual):
        query_itens_pedido = f'SELECT * FROM item_pedido WHERE id_pedido = {id_pedido_atual}'
        resultados = self._retornar_resultados(query_itens_pedido)
        itens_pedido_atual = [ItemPedido(id_item, id_pedido, id_prato, quantidade)
                        for (id_item, id_pedido, id_prato, quantidade)
                        in resultados]
        print([str(item_pedido) for item_pedido in itens_pedido_atual])
        return itens_pedido_atual
