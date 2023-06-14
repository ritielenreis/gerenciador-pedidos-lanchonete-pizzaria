class PrecoItemPedido:
    def __init__(self, preco: float, quantidade: int):
        self._preco = preco
        self._quantidade = quantidade

    def calcular_preco(self) -> float:
        return self._preco * self._quantidade
