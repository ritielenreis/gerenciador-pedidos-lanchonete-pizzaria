from .repositorio_prato import RepositorioPrato
from objetos.salgado import Salgado


class RepositorioSalgado(RepositorioPrato):
    def __init__(self):
        super().__init__()

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

    def ler_salgado(self, id_prato):
        query_salgado = f"""
            SELECT salgado.id_prato, nome_prato, preco, validade, peso, recheio, massa, tipo_salgado
            FROM salgado
            JOIN prato
                ON salgado.id_prato = prato.id_prato
            WHERE salgado.id_prato = {id_prato};            
        """
        (id_prato, nome_prato, preco, validade, peso, recheio, massa, tipo_salgado) = self._retornar_resultado(query_salgado)
        salgado = Salgado(id_prato, nome_prato, preco, validade, peso, recheio, massa, tipo_salgado)
        return salgado

    def ler_salgados(self):
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
            print(salgado)
        return salgados