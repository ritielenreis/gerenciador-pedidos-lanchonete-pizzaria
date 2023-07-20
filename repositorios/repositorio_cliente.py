from .repositorio import Repositorio
from objetos.cliente import Cliente


class RepositorioCliente(Repositorio):
    def __init__(self):
        super().__init__()

    def criar_cliente(self, nome_cliente: str, telefone: str):
        query = f'INSERT INTO cliente (nome_cliente, telefone) VALUES ("{nome_cliente}", "{telefone}");'
        self._executar_query(query)
        query1 = f'SELECT id_cliente FROM cliente WHERE telefone = {telefone};'
        id_cliente = self._retornar_resultado(query1)

        if id_cliente == None:
            print(f"[{self.__class__.__name__}] Cliente nao encontrado.")
        else:
            print(f"[{self.__class__.__name__}] Cliente criado.")
        id_cliente_criado = id_cliente[0]
        return id_cliente_criado

    def ler_cliente(self, id_cliente):
        query_info_cliente = f'''
                SELECT cliente.id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos
                FROM cliente WHERE id_cliente = {id_cliente};'''

        (id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos) = self._retornar_resultado(
            query_info_cliente
        )

        cliente = Cliente(id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos)

        return cliente

    def validar_cliente(self, telefone):
        query_info_cliente = f'''
                SELECT cliente.id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos
                FROM cliente WHERE telefone = '{telefone}';'''

        (id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos) = self._retornar_resultado(
            query_info_cliente
        )

        cliente = Cliente(id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos)
        return cliente

    def ler_clientes(self) -> list[Cliente]:
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

    def edit_cliente(self, id_cliente, coluna:str, valor):
        query = f'UPDATE cliente SET {coluna} = "{valor}" WHERE id_cliente = {id_cliente};'
        self._executar_query(query)
        query1 = f'SELECT * from cliente WHERE id_cliente = {id_cliente};'
        cliente_editado = self._retornar_resultado(query1)
        print(cliente_editado)
        return cliente_editado