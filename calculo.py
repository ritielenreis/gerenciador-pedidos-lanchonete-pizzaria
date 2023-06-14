class Calculo:
    #print('Preço por item_pedido, Total, Nota fiscal, Troco.')
    def __init__(self, repositorio_atual):
        self._repositorio_atual = repositorio_atual

    def preco_item_pedido(self, id_pedido_atual):
        return str(self._repositorio_atual.itens_pedido_atual(id_pedido_atual))

    def calculo_preco_itens(self, id_pedido):
        itens_pedido = self._repositorio_atual.itens_pedido_atual(id_pedido)
        precos = []
        for item in itens_pedido:
            precos.append(int(item.preco) * int(item.quantidade))
        return sum(precos)

    def calculo_taxa(self, id_pedido):
        precos = self.calculo_preco_itens(id_pedido)
        calculo_taxa = precos * 0.1
        return calculo_taxa
