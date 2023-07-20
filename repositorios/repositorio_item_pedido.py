from .repositorio import Repositorio
from objetos.item_pedido import ItemPedido
from objetos.info_item_pedido import InfoItemPedido
from typing import List


class RepositorioItemPedido(Repositorio):
    def __init__(self):
        super().__init__()

    def add_itens_pedido(self, id_pedido, id_prato, quantidade):
        query = f'INSERT INTO item_pedido (id_pedido, id_prato, quantidade) VALUES({id_pedido}, {id_prato}, {quantidade});'
        self._executar_query(query)
        print(f' Prato {id_prato} adicionado ao pedido {id_pedido}!')

    def ler_itens_pedidos(self):
        query_item_pedido = """
            SELECT  id_pedido, id_item,  id_prato, quantidade
           FROM item_pedido;          
        """
        resultados = self._retornar_resultados(query_item_pedido)
        itens_pedido = []
        for (id_pedido, id_item,  id_prato, quantidade) in resultados:
            item_pedido = ItemPedido(id_pedido, id_item,  id_prato, quantidade)
            itens_pedido.append(item_pedido)
            print(item_pedido)
        return itens_pedido

    def ler_itens_pedido(self, id_pedido):
        query_itens_pedido = f'''SELECT id_pedido, id_item,  id_prato, quantidade
                                 FROM item_pedido WHERE id_pedido = {id_pedido};'''

        resultados = self._retornar_resultados(query_itens_pedido)
        itens_pedido = []
        for (id_pedido, id_item,  id_prato, quantidade) in resultados:
            item_pedido = ItemPedido(id_pedido, id_item,  id_prato, quantidade)
            itens_pedido.append(item_pedido)
            print(item_pedido)

        return itens_pedido

    def info_item(self, id_pedido, id_item):
        query_info_item = f'''SELECT id_pedido, id_item,  id_prato, quantidade FROM item_pedido
                              WHERE id_pedido = {id_pedido} and id_item = {id_item};'''
        (id_pedido, id_item,  id_prato, quantidade) = self._retornar_resultado(query_info_item)
        item = ItemPedido(id_pedido, id_item,  id_prato, quantidade)
        print(item)
        return item



    def ler_info_itens_pedido(self, id_pedido) -> List[InfoItemPedido]:
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

    def edit_item_pedido(self, id_pedido, id_item, nova_quantidade):
        query = f'UPDATE item_pedido SET quantidade = {nova_quantidade} WHERE id_pedido = {id_pedido} and id_item = {id_item};'
        self._executar_query(query)
        query1 = f'SELECT * from item_pedido WHERE id_pedido = {id_pedido} and id_item = {id_item};'
        item_editado = self._retornar_resultado(query1)
        print(item_editado)
        return item_editado


