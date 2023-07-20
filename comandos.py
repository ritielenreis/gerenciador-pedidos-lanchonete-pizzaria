from repositorios.repositorio import Repositorio
from repositorios.repositorio_item_pedido import RepositorioItemPedido
from repositorios.repositorio_pizza import RepositorioPizza
from repositorios.repositorio_lanche import RepositorioLanche
from repositorios.repositorio_prato import RepositorioPrato
from repositorios.repositorio_salgado import RepositorioSalgado
from repositorios.repositorio_pedido import RepositorioPedido
from repositorios.repositorio_cliente import RepositorioCliente

    ###Definindo qual será a base de dados usada em cada função (repositório)

repositorio = Repositorio()
repositorio_cliente = RepositorioCliente()
repositorio_pedido = RepositorioPedido()
repositorio_prato = RepositorioPrato()
repositorio_item_pedido = RepositorioItemPedido()
repositorio_pizza = RepositorioPizza()
repositorio_salgado = RepositorioSalgado()
repositorio_lanche = RepositorioLanche()

    ###Testando Repositórios
# Cliente


'''
criar_cliente = repositorio_cliente.criar_cliente('Joana Carmen', 915398728)

editar_cliente = repositorio_cliente.edit_cliente(id_cliente=27, coluna="nome_cliente", valor="Mariana roberta")  #funciona

cliente = repositorio_cliente.ler_clientes()

cliente = repositorio_cliente.ler_cliente(21)
print(cliente)

del_cliente = repositorio_cliente.deletar('cliente', 'id_cliente', 31)

'''



# Pedido

'''
criar_pedido = repositorio_pedido.criar_pedido(15)

ler_pedido = repositorio_pedido.ler_pedidos()

ler_pedido = repositorio_pedido.ler_pedido(5)
print(ler_pedido)

edit_pedido = repositorio_pedido.edit_status_pedido(1)

del_pedido = repositorio_pedido.deletar('pedido', 'id_pedido', 41)
'''



# Item Pedido
'''
add_item_pedido = repositorio_item_pedido.add_itens_pedido(1, 24, 3)

ler_itens_pedidos = repositorio_item_pedido.ler_itens_pedidos()

ler_itens_pedido = repositorio_item_pedido.ler_itens_pedido(6)

ler_item_pedido = repositorio_item_pedido.info_item(2, 4)

edit_item_pedido = repositorio_item_pedido.edit_item_pedido(14, 27, 8)

ler_info_itens_pedido = repositorio_item_pedido.ler_info_itens_pedido(6)
print(ler_info_itens_pedido)

del_item = repositorio_item_pedido.deletar('item_pedido', 'id_item', 45)
'''



# Prato
'''
criar_prato = repositorio_prato.criar_prato('Arroz de carreteiro', 12.00, 3, 100)

prato = repositorio_prato.ler_pratos()

prato = repositorio_prato.ler_prato(58)
print(prato)

del_prato = repositorio_prato.deletar('prato', 'id_prato', 74)
'''


# Lanche
'''
repositorio_lanche.criar_lanche('Sandes de Leitão', 13, 3, 200, 'Pão Caco', '{"tipo": "Leitão desfiado", "queijo": "Branco"}', '{"barbecue": true, "mostarda": true}')

lanches = repositorio_lanche.ler_lanches()

lanche = repositorio_lanche.ler_lanche(62)
print(lanche)

edit_lanche = repositorio_lanche.editar_pratos('lanche', 57, 'pao', 'Pão Integral')

del_lanche = repositorio_lanche.deletar('lanche', 'id_prato', 76)
'''



# Salgado
'''
salgados = repositorio_salgado.ler_salgados()

salgado = repositorio_salgado.ler_salgado(16)
print(salgado)

edit_salgado = repositorio_salgado.editar_pratos('salgado', 67, 'massa', 'Massa folhada')

'''


# Pizza
'''
pizzas = repositorio_pizza.ler_pizzas()
pizza = repositorio_pizza.ler_pizza(8)
print(pizza)

edit_pizza = repositorio_pizza.editar_pratos('pizza', 43, 'molho', 'Provolone')
'''

    ## Testando Menus


#calculo = Calculo(repositorio_atual)
#cliente = repositorio_atual.info_cliente(28)

#editar_item = repositorio_edit.edit_item_pedido(1, 3, 5)
#editar_pratos = repositorio_edit.edit_pratos('prato', 36, 'preco', 33.95)
#editar_lanche = repositorio_edit.edit_pratos('lanche', 62, 'pao', 'Pão Caco')
#editar_pizza = repositorio_edit.edit_pratos('pizza', 43, 'borda', 'cheddar')
#deletar = repositorio_edit.deletar('cliente', 'id_cliente', 26)
#b001 = rep_cliente.criar_cliente('Mariana Rios', 351910344989)

    ###Ver itens do pedido desejado
#repositorio_atual.itens_pedido_atual(1)


    ###Calcular o preço total dos itens do pedido desejado
#repositorio_atual.calculo_preco_itens(1)

    ###Calcular o valor da taxa de serviço do pedido desejado
#repositorio_atual.calculo_taxa(1)

    ###Visualizar pedido atual
#repositorio_atual.pedido_atual(1)

    ###Visualizar fatura
#nota_fiscal.pagamento(1)

    ###Ver cardápio
#cardapio_cliente = Cardapio(repositorio)
#cardapio_cliente.cardapio()


#menu = MenuADM(repositorio)
#menu.menu_adm()

#repositorio_edit.criar_cliente('Ritielen', '910344978')
#repositorio_edit.add_itens_pedido(38, 17, 1)
#print(repositorio_edit.criar_prato('Pizza de Frango com Cebola e Mangericão', 30.90, 7, '700g'))
#repositorio_edit.criar_pizza('Pizza de Calabresa com Cebola e Manjericão', 30.90, 7, '700g', 'molho pesto', '{"sabores": ["calabresa", "cebola", "mangericão"]}', 'catupiry')
#repositorio_edit.criar_lanche('Sandes de Carne Moída com Queijo fresco', 11.90, 3, '150g', 'Pão 7 grãos', '{"tipo": "Carne Moída", "queijo": "Coalho", "vegetais": ["alface", "tomate", "cenoura"]}', '{"mostarda": true, "maionese": true}')
#repositorio_edit.criar_salgado('Pastel de Barbecue', 3.00, 1, '50g', '{"tipo": "Pastel", "recheio": "Queijo Catupiry"}', 'Massa de Batata', 1)
