from tabulate import tabulate
from servico_adm import ServicoAdm
from menu_cliente import MenuCliente
from typing import List

class MenuADM():
    def __init__(self):
        self._servico_adm = ServicoAdm()

    def ver_opcoes(self, pagina):
        print('\n', '=' * 20, f'{pagina}s'.upper(), '=' * 20, ' \n')
        print(f'Criar {pagina}s \t[1] \nVer lista de {pagina}s  \t[2] \nPesquisar {pagina} por ID  \t[3] \nEditar {pagina}s  '
              f'\t[4] \nDeletar {pagina}  \t[5] \nVoltar ao menu inicial   \t[6] \n')

    def menu_adm(self):
        print('\n', '=' * 20, 'GERENCIADOR', '=' * 20, ' \n')
        print('Pedidos \t[1] \nPratos  \t[2] \nClientes   \t[3] \n')
        while True:
            escolha = int(input('O que você gostaria de acessar?'))
            if escolha == 1:
                self.acessar_pedidos()
                break
            elif escolha == 2:
                self.acessar_pratos()
                break
            elif escolha == 3:
                self.acessar_clientes()
                break
            else:
                print('Opção inválida')

    def menu_aux(self):
        print('Editar \t[1] \nVer Pratos  \t[2] \nVoltar ao menu inicial   \t[3] \n')
        while True:
            escolha = int(input('O que você gostaria de acessar?'))
            if escolha == 1:
                self.ler_pedidos()
                break
            elif escolha == 2:
                self.acessar_pratos()
                break
            elif escolha == 3:
                self.menu_adm()
                break
            else:
                print('Opção inválida')

    def acessar_pedidos(self):
        self.ver_opcoes('pedido')
        while True:
            escolha = int(input('O que você gostaria de fazer?'))
            if escolha == 1:
                menu = MenuCliente
                menu.cardapio()
            elif escolha == 2:
                self.ler_pedidos()
                self.menu_adm()
                break
            elif escolha == 3:
                id_pedido = int(input('Qual o ID do pedido desejado?'))
                info_pedido = [str(self._servico_adm.ler_pedido(id_pedido)).split(",")]
                print(tabulate(info_pedido, headers=('Id_pedido', 'Id_cliente', 'Nome_cliente', 'Status')))
                self.menu_adm()
                break
            elif escolha == 4:
                id_pedido = int(input('Qual o ID do pedido que deseja editar?'))
                self._servico_adm.editar_pedido(id_pedido)
                self.menu_adm()
                break
            elif escolha == 5:
                id_pedido_deletado = int(input('Qual o ID do pedido que deseja deletar?'))
                self._servico_adm.del_pedido('id_pedido', id_pedido_deletado)
                self.menu_adm()
                break
            elif escolha == 6:
                self.menu_adm()
                break
            else:
                print('Opção inválida')

    def ler_pedidos(self):
        pedidos = self._servico_adm.ler_pedidos()
        table_pedidos = []
        for pedido in pedidos:
            table_pedidos.append([pedido._id_cliente, pedido.id_pedido, pedido.status])
        print(tabulate(table_pedidos, headers=('ID Cliente', 'ID Pedido', 'Status')))
        self.menu_adm()
        return table_pedidos

    def acessar_pratos(self):
        self.ver_opcoes('prato')
        while True:
            escolha = int(input('O que você gostaria de fazer?'))
            if escolha == 1:
                self.criar_pratos()
            elif escolha == 2:
                self.ler_pratos()
                break
            elif escolha == 3:
                id_prato = int(input('Qual o ID do prato desejado?'))
                info_prato = [str(self._servico_adm.ler_prato(id_prato)).split(",")]
                print(tabulate(info_prato, headers=('Id_prato', 'Nome_prato', 'Preço', 'Quantidade', 'Peso')))
                self.menu_adm()
                break
            elif escolha == 4:
                id_prato = int(input('Qual o ID do prato que deseja editar?'))
                coluna = str(input('Qual a coluna do prato que deseja editar?'))
                valor = str(input('Digite o novo valor?'))
                self._servico_adm.editar_prato(id_prato, coluna, valor)
                break
            elif escolha == 5:
                id_prato_deletado = int(input('Qual o ID do prato que deseja deletar?'))
                self._servico_adm.del_prato(id_prato_deletado)
                break
            elif escolha == 6:
                self.menu_adm()
                break
            else:
                print('Opção inválida')

    def criar_pratos(self):
        print('\n', '=' * 20, 'CRIAR PRATO', '=' * 20, ' \n')
        print(f'Lanche \t[1] \nPizza \t[2] \nSalgado \t[3] \n')
        while True:
            escolha = int(input('O que você gostaria de criar?'))
            if escolha == 1:
                nome_prato = str(input('Nome do Prato:'))
                preco = str(input('Preço:'))
                validade = str(input('Validade'))
                peso = str(input('Peso:'))
                pao = str(input('Pão:'))
                recheio = str(input('Recheio:'))
                molhos = str(input('Molhos:'))

                self._servico_adm.criar_lanche(nome_prato, preco, validade, peso, pao, recheio, molhos)
                break
            elif escolha == 2:
                nome_prato = str(input('Nome do Prato:'))
                preco = str(input('Preço:'))
                validade = str(input('Validade'))
                peso = str(input('Peso:'))
                molho = str(input('Molho:'))
                recheio = str(input('Recheio:'))
                borda = str(input('Borda:'))

                self._servico_adm.criar_pizza(nome_prato, preco, validade, peso, molho, recheio, borda)
                break
            elif escolha == 3:
                nome_prato = str(input('Nome do Prato:'))
                preco = str(input('Preço:'))
                validade = str(input('Validade'))
                peso = str(input('Peso:'))
                recheio = str(input('Recheio:'))
                massa = str(input('Massa:'))
                tipo_salgado = str(input('Tipo de Salgado:'))

                self._servico_adm.criar_salgado(nome_prato, preco, validade, peso, recheio, massa, tipo_salgado)
                break
            else:
                print('Opção inválida')

    def acessar_clientes(self):
        self.ver_opcoes('cliente')
        while True:
            escolha = int(input('O que você gostaria de fazer?'))
            if escolha == 1:
                self.criar_cliente()
                self.menu_adm()
            elif escolha == 2:
                self.ler_clientes()
                self.menu_adm()
                break
            elif escolha == 3:
                id_cliente = int(input('Qual o ID do pedido desejado?'))
                info_cliente = [str(self._servico_adm.ler_cliente(id_cliente)).split(",")]
                print(tabulate(info_cliente, headers=('Id_cliente', 'Nome_cliente', 'Telefone')))
                self.menu_adm()
                break
            elif escolha == 4:
                id_cliente = int(input('Qual o ID do cliente que deseja editar?'))
                coluna = str(input('Qual o dado do cliente você deseja editar?'))
                valor = str(input('Digite o novo valor?'))
                self._servico_adm.editar_cliente(id_cliente, coluna, valor)
                self.menu_adm()
                break
            elif escolha == 5:
                id_cliente_deletado = int(input('Qual o ID do cliente que deseja deletar?'))
                self._servico_adm.del_cliente(id_cliente_deletado)
                self.menu_adm()
                break
            elif escolha == 6:
                self.menu_adm()
                break
            else:
                print('Opção inválida')

    def ler_clientes(self):
        clientes = self._servico_adm.ler_clientes()
        table_clientes = []
        for cliente in clientes:
            table_clientes.append([cliente.id_cliente, cliente.nome_cliente, cliente.telefone])
        print(tabulate(table_clientes, headers=('ID Cliente', 'Nome Cliente', 'Telefone')))
        self.menu_adm()
        return table_clientes

    def criar_cliente(self):
        nome = str(input('Nome:'))
        telefone = str(input('Telefone:'))
        id_cliente_criado = self._servico_adm.criar_cliente(nome, telefone)
        cliente = self._servico_adm.ler_cliente(id_cliente_criado)
        print(f' Cliente {cliente.nome_cliente}  ID {cliente.id_cliente}', end='')
        return cliente.id_cliente

    def ler_pratos(self):
        lanches = self._servico_adm.ler_lanches()
        salgados = self._servico_adm.ler_salgados()
        pizzas = self._servico_adm.ler_pizzas()
        table_pratos = []
        for lanche in lanches:
            table_pratos.append([lanche.id_prato, lanche.nome_prato, lanche.preco])
        for salgado in salgados:
            table_pratos.append([salgado.id_prato, salgado.nome_prato, salgado.preco])
        for pizza in pizzas:
            table_pratos.append([pizza.id_prato, pizza.nome_prato, pizza.preco])
        print(tabulate(table_pratos, headers=('ID Prato', 'Nome Prato', 'Preço')))
        self.menu_adm()
