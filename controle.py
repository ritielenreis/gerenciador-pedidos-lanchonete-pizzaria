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





