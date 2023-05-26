from item_pedido import ItemPedido
from pedido import Pedido
from cliente import Cliente
from pizza import Pizza
from lanche import Lanche
from salgado import Salgado
from prato import Prato
from repositorio import Repositorio


pedido_desejado = pedidos[2]
print(f'\n\n\n' )
print(pedido_desejado)


def encontrar_prato(id_prato):
    for prato in pratos:
        if prato.id_prato == id_prato:
            return prato

    raise Exception("Prato nao encontrado")

lista_preco_quantidade = []
for item_pedido in itens_pedido_desejado:
    prato = encontrar_prato(item_pedido.id_prato)
    print("\tPrato encontrado:", prato)

    preco = prato.preco
    quantidade = item_pedido.quantidade
    print("\tQuantidade:", quantidade)
    lista_preco_quantidade.append((preco, quantidade))

def calcular_valor_total_pedido(precos_quantidades):
    valor_total = 0
    for preco, quantidade in precos_quantidades:
        valor_total += preco * quantidade

    return valor_total

print("Taxa de servico", pedido_desejado.taxa_servico)
montante = calcular_valor_total_pedido(lista_preco_quantidade)
print("Montante do pedido", montante)

valor_total = montante + pedido_desejado.taxa_servico
print(f"Valor total do pedido: {valor_total}")



