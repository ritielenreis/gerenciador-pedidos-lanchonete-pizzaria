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

class ServicoAdm:
    def __init__(self):
        self._repositorio_cliente = RepositorioCliente()
        self._repositorio_adm = RepositorioAdm()
        self._repositorio_pizza = RepositorioPizza()
        self._repositorio_lanche = RepositorioLanche()
        self._repositorio_salgado = RepositorioSalgado()
        self._repositorio_prato = RepositorioPrato()
        self._repositorio_pedido = RepositorioPedido()
        self._repositorio_item_pedido = RepositorioItemPedido()

    def criar_funcionario(self, nome_funcionario, senha):
        adm = self._repositorio_adm.criar_funcionario(nome_funcionario, senha)
        return adm

    def validar_adm(self, id_adm, senha):
        adm = self._repositorio_adm.validar_adm(id_adm, senha)
        return adm

    def criar_cliente(self, nome, telefone):
        cliente = self._repositorio_cliente.criar_cliente(nome, telefone)
        return cliente

    def ler_cliente(self, id_cliente):
        cliente = self._repositorio_cliente.ler_cliente(id_cliente)
        return cliente

    def ler_clientes(self):
        clientes = self._repositorio_cliente.ler_clientes()
        return clientes

    def editar_cliente(self, id_cliente, coluna, valor):
        cliente = self._repositorio_cliente.edit_cliente(id_cliente, coluna, valor)
        return cliente

    def validar_cliente(self, telefone):
        cliente = self._repositorio_cliente.validar_cliente(telefone)
        return cliente

    def del_cliente(self, id_cliente):
        cliente = self._repositorio_cliente.deletar(table='cliente', nome_id='id_cliente', valor_id=id_cliente)
        return cliente

    def ler_prato(self, id_prato):
        prato = self._repositorio_prato.ler_prato(id_prato)
        return prato

    def ler_pratos(self):
        pratos = self._repositorio_prato.ler_pratos()
        return pratos

    def editar_prato(self, id_prato, coluna, valor):
        prato = self._repositorio_prato.editar_pratos(tabela='prato', id_prato=id_prato, coluna=coluna, valor=valor)
        return prato

    def del_prato(self, valor_id):
        prato = self._repositorio_prato.deletar(table='prato', nome_id='id_prato', valor_id=valor_id)
        return prato

    def criar_pizza(self, nome_prato, preco, validade, peso, molho, recheio, borda):
        pizza = self._repositorio_pizza.criar_pizza(nome_prato, preco, validade, peso, molho, recheio, borda)
        return pizza

    def ler_pizza(self, id_pizza):
        pizza = self._repositorio_pizza.ler_pizza(id_pizza)
        return pizza

    def ler_pizzas(self):
        pizzas = self._repositorio_pizza.ler_pizzas()
        return pizzas

    def editar_pizza(self, id_prato, coluna, valor):
        pizza = self._repositorio_pizza.editar_pratos(tabela='pizza', id_prato=id_prato, coluna=coluna, valor=valor)
        return pizza

    def del_pizza(self, valor_id):
        pizza = self._repositorio_pizza.deletar(table='pizza', nome_id='id_prato', valor_id=valor_id)
        return pizza

    def criar_lanche(self, nome_prato, preco, validade, peso, pao, recheio, molhos):
        lanche = self._repositorio_lanche.criar_lanche(nome_prato, preco, validade, peso, pao, recheio, molhos)
        return lanche

    def ler_lanche(self, id_lanche):
        pizza = self._repositorio_lanche.ler_lanche(id_lanche)
        return pizza

    def ler_lanches(self):
        lanches = self._repositorio_lanche.ler_lanches()
        return lanches

    def editar_lanche(self, id_prato, coluna, valor):
        lanche = self._repositorio_lanche.editar_pratos(tabela='lanche', id_prato=id_prato, coluna=coluna, valor=valor)
        return lanche

    def del_lanche(self, valor_id):
        lanche = self._repositorio_lanche.deletar(table='lanche', nome_id='id_prato', valor_id=valor_id)
        return lanche

    def criar_salgado(self, nome_prato, preco, validade, peso, recheio, massa, tipo_salgado):
        salgado = self._repositorio_salgado.criar_salgado(nome_prato, preco, validade, peso, recheio, massa, tipo_salgado)
        return salgado

    def ler_salgado(self, id_salgado):
        salgado = self._repositorio_salgado.ler_salgado(id_salgado)
        return salgado

    def ler_salgados(self):
        salgados = self._repositorio_salgado.ler_salgados()
        return salgados

    def editar_salgado(self, id_prato, coluna, valor):
        salgado = self._repositorio_salgado.editar_pratos(tabela='salgado', id_prato=id_prato, coluna=coluna, valor=valor)
        return salgado

    def del_salgado(self, valor_id):
        salgado = self._repositorio_salgado.deletar(table='salgado', nome_id='id_prato', valor_id=valor_id)
        return salgado

    def criar_pedido(self, id_cliente):
        pedido = self._repositorio_pedido.criar_pedido(id_cliente)
        return pedido

    def ler_pedido(self, id_pedido):
        pedido = self._repositorio_pedido.ler_pedido(id_pedido)
        return pedido

    def ler_pedidos(self):
        pedidos = self._repositorio_pedido.ler_pedidos()
        return pedidos

    def editar_pedido(self, id_pedido):
        pedido = self._repositorio_pedido.edit_status_pedido(id_pedido)
        return pedido

    def del_pedido(self, nome_id, valor_id):
        pedido = self._repositorio_pedido.deletar(table='pedido', nome_id='id_pedido', valor_id=valor_id)
        return pedido

    def criar_item_pedido(self, id_pedido, id_prato, quantidade):
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
