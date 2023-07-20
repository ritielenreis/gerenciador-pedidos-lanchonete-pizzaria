from repositorios import (
    RepositorioAdm,
    RepositorioCliente,
    RepositorioPrato,
    RepositorioPizza,
    RepositorioSalgado,
    RepositorioLanche,
    RepositorioPedido,
    RepositorioItemPedido
)


class Calculo:
    #print('Preço por item_pedido, Total, Nota fiscal, Troco.')
    def __init__(self):
        self._repositorio_cliente = RepositorioCliente()
        self._repositorio_adm = RepositorioAdm()
        self._repositorio_pizza = RepositorioPizza()
        self._repositorio_lanche = RepositorioLanche()
        self._repositorio_salgado = RepositorioSalgado()
        self._repositorio_prato = RepositorioPrato()
        self._repositorio_pedido = RepositorioPedido()
        self._repositorio_item_pedido = RepositorioItemPedido()

    def preco_item_pedido(self, id_pedido_atual):
        return str(self._repositorio_item_pedido.ler_itens_pedido(id_pedido_atual))

    def calculo_preco_itens(self, id_pedido):
        itens_pedido = self._repositorio_item_pedido.ler_info_itens_pedido(id_pedido)
        precos = []
        for item in itens_pedido:
            precos.append(int(item.preco) * int(item.quantidade))
        return sum(precos)

    def calculo_taxa(self, id_pedido):
        precos = self.calculo_preco_itens(id_pedido)
        calculo_taxa = precos * 0.1
        return calculo_taxa
