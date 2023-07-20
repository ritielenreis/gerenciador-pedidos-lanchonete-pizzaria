from .repositorio import Repositorio
from objetos.pedido import Pedido
from objetos.pedido_info import PedidoInfo


class RepositorioPedido(Repositorio):
    def __init__(self):
        super().__init__()

    def criar_pedido(self, id_cliente: int):
        query = f'INSERT INTO pedido (id_cliente) VALUES({id_cliente});'
        self._executar_query(query)
        query1 = f"SELECT MAX(id_pedido) FROM pedido WHERE id_cliente = {id_cliente};"
        linha = self._retornar_resultado(query1)

        if linha == None:
            print(f"[{self.__class__.__name__}] Pedido nao encontrado.")
        id_pedido = linha[0]

        print(f"[{self.__class__.__name__}] Pedido criado.")
        return id_pedido

    def ler_pedido(self, id_pedido):
        query_pedido = f"""
            SELECT pedido.id_cliente, cliente.nome_cliente, pedido.id_pedido, pedido.status
            FROM pedido
            JOIN cliente ON pedido.id_cliente = cliente.id_cliente
            WHERE pedido.id_pedido = {id_pedido};          
        """
        (id_cliente, nome_cliente, id_pedido, status) = self._retornar_resultado(query_pedido)
        pedido = PedidoInfo(id_cliente, nome_cliente, id_pedido, status)
        return pedido

    def ler_pedidos(self):
        query_pedidos = """
                    SELECT pedido.id_cliente, pedido.id_pedido, pedido.status
                    FROM pedido;          
                """
        resultados = self._retornar_resultados(query_pedidos)
        pedidos = []
        for (id_cliente, id_pedido, status) in resultados:
            pedido = Pedido(id_cliente, id_pedido, status)
            pedidos.append(pedido)
        return pedidos

    def edit_status_pedido(self, id_pedido):
        query_status = f'SELECT status from pedido WHERE id_cliente = {id_pedido};'
        status = str(self._executar_query(query_status))
        if status == 'pendente' or 'None':
            query = f"UPDATE pedido SET status = 'concluído' WHERE id_pedido = {id_pedido};"
            self._executar_query(query)
        query1 = f'SELECT status from pedido WHERE id_pedido = {id_pedido};'
        pedido_concluido = self._retornar_resultado(query1)
        print(f'Pedido {id_pedido} {pedido_concluido[0]}')
        return pedido_concluido
