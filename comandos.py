from repositorio import Repositorio
from repositorio_atual import RepositorioAtual
from repositorio_edit import RepositorioEdit
from cardapio import Cardapio
from nota_fiscal import NotaFiscal
from calculo import Calculo
from menu_adm import MenuADM

    ###Definindo qual será a base de dados usada em cada função (repositório)
repositorio_atual = RepositorioAtual()
repositorio_edit = RepositorioEdit()
repositorio = Repositorio()

nota_fiscal = NotaFiscal(repositorio_atual)
#calculo = Calculo(repositorio_atual)
#cliente = repositorio_atual.info_cliente(28)
#editar_cliente = repositorio_edit.edit_cliente(id_cliente=25, coluna="nome_cliente", valor="Mariana Almeida")
#editar_item = repositorio_edit.edit_item_pedido(1, 3, 5)
#editar_pratos = repositorio_edit.edit_pratos('prato', 36, 'preco', 33.95)
#editar_lanche = repositorio_edit.edit_pratos('lanche', 62, 'pao', 'Pão Caco')
#editar_pizza = repositorio_edit.edit_pratos('pizza', 43, 'borda', 'cheddar')
deletar = repositorio_edit.deletar('cliente', 'id_cliente', 26)

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
