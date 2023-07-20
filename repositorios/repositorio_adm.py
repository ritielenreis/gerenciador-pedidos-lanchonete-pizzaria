from .repositorio import Repositorio
from objetos.adm import Adm


class RepositorioAdm(Repositorio):
    def __init__(self):
        super().__init__()

    def criar_funcionario(self, nome_funcionario: str, senha: str):
        query = f'INSERT INTO cliente (nome_uncionario, senha) VALUES ("{nome_funcionario}", "{senha}");'
        self._executar_query(query)
        query1 = f'SELECT id_adm FROM adm WHERE nome_funcionario = {nome_funcionario};'
        id_funcionario = self._retornar_resultado(query1)

        if id_funcionario == None:
            print(f"[{self.__class__.__name__}] Funcionário nao encontrado.")
        else:
            print(f"[{self.__class__.__name__}] funcionário criado.")
        id_funcionario_criado = id_funcionario[0]
        return id_funcionario_criado

    def validar_adm(self, id_adm, senha):
        query_info_adm = f"SELECT id_adm, nome_adm, senha FROM adm WHERE senha = '{senha}' and id_adm =  {id_adm};"
        resultado = self._retornar_resultado(query_info_adm)
        (id_adm, nome_adm, senha) = resultado
        adm = Adm(id_adm, nome_adm, senha)
        return adm

    def ler_adm(self, id_adm):
        query_info_adm = f'SELECT id_adm, nome_adm, senha FROM adm WHERE id_adm = {id_adm};'
        (id_adm, nome_adm, senha) = self._retornar_resultado(query_info_adm)
        adm = Adm(id_adm, nome_adm, senha)
        funcionario = (adm.id_adm, adm.nome_adm)
        return adm


    '''
    def ler_cliente(self, id_cliente):
        query_info_cliente = f'
                SELECT adm.id_cliente, nome_cliente, telefone, rua, cidade, cod_postal, historico_pedidos
                FROM cliente WHERE id_cliente = {id_cliente};'

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
            print(cliente)
        return clientes

    def edit_cliente(self, id_cliente, coluna:str, valor):
        query = f'UPDATE cliente SET {coluna} = "{valor}" WHERE id_cliente = {id_cliente};'
        self._executar_query(query)
        query1 = f'SELECT * from cliente WHERE id_cliente = {id_cliente};'
        cliente_editado = self._retornar_resultado(query1)
        print(cliente_editado)
        return cliente_editado'''