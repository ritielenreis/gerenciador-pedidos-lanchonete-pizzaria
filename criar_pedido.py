from repositorio import Repositorio


class CriarPedido:
    def executar(self, id_cliente: int):
        repositorio = Repositorio()
        cliente = repositorio.cliente_por(id_cliente=id_cliente)
        pedido = repositorio.criar_pedido(id_cliente=cliente.id_cliente)

criarPedido = CriarPedido()
criarPedido.executar(id_cliente=1)
