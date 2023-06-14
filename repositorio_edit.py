from mysql.connector import connect, Error
from item_pedido import ItemPedido
from pedido_info import PedidoInfo
from typing import List
from pedido import Pedido
from repositorio_atual import RepositorioAtual


class RepositorioEdit:
    def __init__(self):
        self.connection = connect(
            user='dono_lanchonete',
            password='uma_senha_forte',
            host='localhost',
            database='lanchonete'
        )

    def _executar_query(self, query):
        try:
            cursor = self.connection.cursor(buffered=True)
            cursor.execute(query)
            self.connection.commit()
        except Error as e:
            self.connection.rollback()
            print(f"[{self.__class__.__name__}] Error:", e)

    def _retornar_resultado(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            return result
        except Error as e:
            print(f"[{self.__class__.__name__}] Error:", e)

    def _retornar_resultados(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"[{self.__class__.__name__}] Error:", e)

    def criar_cliente(self, nome_cliente: str, telefone: str):
        query = f'INSERT INTO cliente (nome_cliente, telefone) VALUES ("{nome_cliente}", "{telefone}");'
        self._executar_query(query)
        query1 = f'SELECT id_cliente FROM cliente WHERE telefone = {telefone};'
        id_cliente = self._retornar_resultado(query1)

        if id_cliente == None:
            print(f"[{self.__class__.__name__}] Cliente nao encontrado.")
        else:
            print(f"[{self.__class__.__name__}] Cliente criado.")
        print(id_cliente[0])
        return id_cliente

    def criar_pedido(self, id_cliente: int):
        query = f'INSERT INTO pedido (id_cliente) VALUES({id_cliente});'
        self._executar_query(query)
        query1 = f"SELECT MAX(id_pedido) FROM pedido WHERE id_cliente = {id_cliente};"
        linha = self._retornar_resultado(query1)

        if linha == None:
            print(f"[{self.__class__.__name__}] Pedido nao encontrado.")
        id_pedido = linha[0]

        print(f"[{self.__class__.__name__}] Pedido criado.")
        return id_pedido


    def add_itens_pedido(self, id_pedido, id_prato, quantidade):
        query = f'INSERT INTO item_pedido (id_pedido, id_prato, quantidade) VALUES({id_pedido}, {id_prato}, {quantidade});'
        self._executar_query(query)
        repositorio = RepositorioAtual()
        item_add = repositorio.itens_pedido_atual(id_pedido)
        print(item_add)

    def criar_prato(self, nome_prato, preco, validade, peso):
        query = f'INSERT INTO prato (nome_prato, preco, validade, peso) VALUES ("{nome_prato}", {preco}, {validade}, "{peso}");'
        self._executar_query(query)
        query1 = f"SELECT id_prato FROM prato WHERE nome_prato = '{nome_prato}';"
        id_prato_ = self._retornar_resultado(query1)

        if id_prato_ == None:
            print(f"[{self.__class__.__name__}] Prato nao encontrado.")
        print(f"[{self.__class__.__name__}] Prato criado.")

        id_prato = id_prato_[0]
        return id_prato

    def criar_pizza(self, nome_prato, preco, validade, peso, molho, recheio, borda):
        id_prato = self.criar_prato(nome_prato, preco, validade, peso)
        query = f"INSERT INTO pizza (id_prato, molho, recheio, borda) VALUES ({id_prato}, '{molho}', '{recheio}', '{borda}');"
        self._executar_query(query)
        query1 = f"SELECT pizza.id_prato FROM pizza JOIN prato on pizza.id_prato=prato.id_prato WHERE nome_prato = '{nome_prato}';"
        id_pizza = self._retornar_resultado(query1)

        if id_pizza == None:
            print(f"[{self.__class__.__name__}] Pizza nao encontrada.")
        print(f"[{self.__class__.__name__}] Pizza encontrada.")

        id_pizza = id_pizza[0]
        return id_pizza

    def criar_lanche(self, nome_prato, preco, validade, peso, pao, recheio, molhos):
        id_prato = self.criar_prato(nome_prato, preco, validade, peso)
        query = f"INSERT INTO lanche (id_prato, pao, recheio, molhos) VALUES ({id_prato}, '{pao}', '{recheio}', '{molhos}');"
        self._executar_query(query)
        query1 = f"SELECT lanche.id_prato FROM lanche JOIN prato on lanche.id_prato=prato.id_prato WHERE nome_prato = '{nome_prato}';"
        id_lanche = self._retornar_resultado(query1)

        if id_lanche == None:
            print(f"[{self.__class__.__name__}] Lanche nao encontrado.")
        else:
            print(f"[{self.__class__.__name__}] Lanche encontrado.")

        id_lanche = id_lanche[0]
        return id_lanche

    def criar_salgado(self, nome_prato, preco, validade, peso, recheio, massa, tipo_salgado):
        id_prato = self.criar_prato(nome_prato, preco, validade, peso)

        query = f"INSERT INTO salgado (id_prato, recheio, massa, tipo_salgado) VALUES ({id_prato}, '{recheio}', '{massa}', {tipo_salgado});"
        self._executar_query(query)
        query1 = f"SELECT salgado.id_prato FROM salgado JOIN prato on salgado.id_prato=prato.id_prato WHERE nome_prato = '{nome_prato}';"
        salgado_tupla = self._retornar_resultado(query1)

        if salgado_tupla == None:
            print(f"[{self.__class__.__name__}] Salgado nao encontrado.")
        else:
            print(f"[{self.__class__.__name__}] Salgado encontrado.")

        id_salgado = int(salgado_tupla[0])
        return id_salgado

    def edit_cliente(self, id_cliente, coluna:str, valor):
        query = f'UPDATE cliente SET {coluna} = "{valor}" WHERE id_cliente = {id_cliente};'
        self._executar_query(query)
        query1 = f'SELECT * from cliente WHERE id_cliente = {id_cliente};'
        cliente_editado = self._retornar_resultado(query1)
        print(cliente_editado)
        return cliente_editado

    def edit_item_pedido(self, id_pedido, id_item, valor):
        query = f'UPDATE item_pedido SET quantidade = {valor} WHERE id_pedido = {id_pedido} and id_item = {id_item};'
        self._executar_query(query)
        query1 = f'SELECT * from item_pedido WHERE id_pedido = {id_pedido} and id_item = {id_item};'
        item_editado = self._retornar_resultado(query1)
        print(item_editado)
        return item_editado

    def edit_pratos(self, tabela, id_prato, coluna:str, valor):
        query = f'UPDATE {tabela} SET {coluna} = "{valor}" WHERE id_prato = {id_prato};'
        self._executar_query(query)
        query1 = f'SELECT * from {tabela} WHERE id_prato = {id_prato};'
        prato_editado = self._retornar_resultado(query1)
        print(prato_editado)
        return prato_editado

    def deletar(self, table, nome_id, valor_id):
        query = f'DELETE FROM {table} WHERE {nome_id} = {valor_id};'
        self._executar_query(query)

        print(f'{table} apagado!')