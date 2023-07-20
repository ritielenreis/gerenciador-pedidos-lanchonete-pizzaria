from .repositorio_prato import RepositorioPrato
from objetos.lanche import Lanche


class RepositorioLanche(RepositorioPrato):
    def __init__(self):
        super().__init__()

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

    def ler_lanche(self, id_prato):
        #Busca todos os dados de pratos que são lanches
        query_lanche = f"""
            SELECT lanche.id_prato, nome_prato, preco, validade, peso, pao, recheio, molhos 
            FROM lanche
            JOIN prato ON lanche.id_prato = prato.id_prato
            WHERE lanche.id_prato = {id_prato};"""
        (id_prato, nome_prato, preco, validade, peso, pao, recheio, molho) = self._retornar_resultado(query_lanche)
        lanche = Lanche(id_prato, nome_prato, preco, validade, peso, pao, recheio, molho)
        return lanche

    def ler_lanches(self):
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
            print(lanche)
        return lanches
