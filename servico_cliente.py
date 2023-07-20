from repositorios.repositorio_cliente import RepositorioCliente
from repositorios.repositorio_prato import RepositorioPrato
from repositorios.repositorio_pizza import RepositorioPizza
from repositorios.repositorio_salgado import RepositorioSalgado
from repositorios.repositorio_lanche import RepositorioLanche
from repositorios.repositorio_pedido import RepositorioPedido
from repositorios.repositorio_item_pedido import RepositorioItemPedido


class ServicoCliente:
    def __init__(self):
        self._repositorio_cliente = RepositorioCliente()
        self._repositorio_pizza = RepositorioPizza()
        self._repositorio_lanche = RepositorioLanche()
        self._repositorio_salgado = RepositorioSalgado()
        self._repositorio_prato = RepositorioPrato()
        self._repositorio_pedido = RepositorioPedido()
        self._repositorio_item_pedido = RepositorioItemPedido()

    def criar_cliente(self, nome, telefone):
        cliente = self._repositorio_cliente.criar_cliente(nome, telefone)
        return cliente

    def validar_cliente(self, telefone):
        cliente = self._repositorio_cliente.validar_cliente(telefone)
        print(f' Cliente {cliente.nome_cliente}  ID {cliente.id_cliente}', end='')
        return cliente

    def ler_prato(self, id_prato):
        salgado = self._repositorio_prato.ler_prato(id_prato)
        return salgado

    def ler_pratos(self):
        pratos = self._repositorio_prato.ler_pratos()
        return pratos

    def ler_pizza(self, id_pizza):
        pizza = self._repositorio_pizza.ler_pizza(id_pizza)
        return pizza

    def ler_pizzas(self):
        pizzas = self._repositorio_pizza.ler_pizzas()
        return pizzas

    def ler_lanche(self, id_lanche):
        pizza = self._repositorio_lanche.ler_lanche(id_lanche)
        return pizza

    def ler_lanches(self):
        lanches = self._repositorio_lanche.ler_lanches()
        return lanches

    def ler_salgado(self, id_salgado):
        salgado = self._repositorio_salgado.ler_salgado(id_salgado)
        return salgado

    def ler_salgados(self):
        salgados = self._repositorio_salgado.ler_salgados()
        return salgados

    def criar_pedido(self, id_cliente):
        pedido = self._repositorio_pedido.criar_pedido(id_cliente)
        return pedido

    def ler_pedido(self, id_pedido):
        pedido = self._repositorio_pedido.ler_pedido(id_pedido)
        return pedido

    def ler_pedidos(self):
        pedidos = self._repositorio_pedido.ler_pedidos()
        return pedidos

    def add_item_pedido(self, id_pedido, id_prato, quantidade):
        item_pedido = self._repositorio_item_pedido.add_itens_pedido(id_pedido, id_prato, quantidade)
        return item_pedido

    def ler_itens_pedido(self, id_pedido):
        itens_pedido = self._repositorio_item_pedido.ler_itens_pedido(id_pedido)
        return itens_pedido

    def ler_item_pedidos(self):
        itens_pedidos = self._repositorio_item_pedido.ler_itens_pedidos()
        return itens_pedidos

    def info_item(self, id_pedido, id_item):
        item_pedido = self._repositorio_item_pedido.info_item(id_pedido, id_item)
        return item_pedido

    def ler_info_itens_pedido(self, id_pedido):
        itens_pedido = self._repositorio_item_pedido.ler_info_itens_pedido(id_pedido)
        return itens_pedido

    def editar_item_pedido(self, id_pedido, id_item, nova_quantidade):
        item_pedido = self._repositorio_item_pedido.edit_item_pedido(id_pedido, id_item, nova_quantidade)
        return item_pedido

    def del_item_pedido(self, valor_id):
        item_pedido = self._repositorio_item_pedido.deletar(table='item_pedido', nome_id='id_pedido', valor_id=valor_id)
        return item_pedido
