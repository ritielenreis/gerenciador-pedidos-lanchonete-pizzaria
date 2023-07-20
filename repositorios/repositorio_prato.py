from .repositorio import Repositorio
from objetos.prato import Prato


class RepositorioPrato(Repositorio):
    def __init__(self):
        super().__init__()

    def criar_prato(self, nome_prato, preco, validade, peso):
        query = f'INSERT INTO prato (nome_prato, preco, validade, peso) VALUES ("{nome_prato}", {preco}, {validade}, "{peso}");'
        self._executar_query(query)
        query1 = f"SELECT id_prato FROM prato WHERE nome_prato = '{nome_prato}';"
        id_prato_ = self._retornar_resultado(query1)
        id_prato = id_prato_[0]

        if id_prato_ == None:
            print(f"[{self.__class__.__name__}] Prato nao encontrado.")
        print(f"[{self.__class__.__name__}] Prato {id_prato} criado.")
        return id_prato

    def ler_prato(self, id_prato):
        query_clientes = f"SELECT id_prato, nome_prato, preco, validade, peso FROM prato WHERE id_prato = {id_prato};"
        (id_prato, nome_prato, preco, validade, peso) = self._retornar_resultado(query_clientes)
        prato = Prato(id_prato, nome_prato, preco, validade, peso)
        return prato

    def ler_pratos(self):
        query_pratos = "SELECT id_prato, nome_prato, preco, validade, peso FROM prato;"
        resultados = self._retornar_resultados(query_pratos)
        pratos = []
        for (id_prato, nome_prato, preco, validade, peso) in resultados:
            prato = Prato(id_prato, nome_prato, preco, validade, peso)
            pratos.append(prato)
            print(prato)
        return pratos

    def editar_pratos(self, tabela, id_prato, coluna:str, valor):
        query = f'UPDATE {tabela} SET {coluna} = "{valor}" WHERE id_prato = {id_prato};'
        self._executar_query(query)
        query1 = f'SELECT * from {tabela} WHERE id_prato = {id_prato};'
        prato_editado = self._retornar_resultado(query1)
        print(prato_editado)
        return prato_editado