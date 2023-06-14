from tabulate import tabulate
from calculo import Calculo
from repositorio import Repositorio
from repositorio_edit import RepositorioEdit


class MenuADM:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def menu_adm(self):
        print('\n', '=' * 20, 'GERENCIADOR', '=' * 20, ' \n')
        print('Pedidos \t[1] \nPratos  \t[2] \nClientes   \t[3] \n')
        while True:
            escolha = int(input('O que você gostaria de acessar?'))
            if escolha == 1:
                self.list_pedidos()
                break
            elif escolha == 2:
                self.list_pratos()
                break
            elif escolha == 3:
                self.list_clientes()
                break
            else:
                print('Opção inválida')

    def menu_aux(self):
        print('Editar \t[1] \nPratos  \t[2] \nVoltar ao menu inicial   \t[3] \n')
        while True:
            escolha = int(input('O que você gostaria de acessar?'))
            if escolha == 1:
                self.list_pedidos()
                break
            elif escolha == 2:
                self.list_pratos()
                break
            elif escolha == 3:
                self.menu_adm()
                break
            else:
                print('Opção inválida')

    def menu_cliente(self):
        print('\n', '=' * 20, 'CADASTRO DE CLIENTE', '=' * 20, ' \n')
        print('Já tenho cadastro na loja \t[1] \nAinda não tenho  \t[2] \n')
        rep_cliente = RepositorioEdit()
        while True:
            escolha = int(input('Você já tem cadastro na loja?'))
            if escolha == 1:
                break
            elif escolha == 2:
                self.list_pratos()
                break
            elif escolha == 3:
                self.list_clientes()

                break
            else:
                print('Opção inválida')


    def list_pedidos(self):
        pedidos = self.repositorio.pedidos()
        table_pedidos = []
        for pedido in pedidos:
            table_pedidos.append([pedido._id_cliente, pedido.id_pedido, pedido.status])
        print(tabulate(table_pedidos, headers=('ID Cliente', 'ID Pedido', 'Status')))
        self.menu_adm()
        return table_pedidos

    def list_clientes(self):
        clientes = self.repositorio.clientes()
        table_clientes = []
        for cliente in clientes:
            table_clientes.append([cliente.id_cliente, cliente.nome_cliente, cliente.telefone])
        print(tabulate(table_clientes, headers=('ID Cliente', 'Nome Cliente', 'Telefone')))
        self.menu_adm()
        return table_clientes

    def list_pratos(self):
        lanches = self.repositorio.lanches()
        salgados = self.repositorio.salgados()
        pizzas = self.repositorio.pizzas()
        table_pratos = []
        table_salgados = []
        table_pizzas = []
        for lanche in lanches:
            table_pratos.append([lanche.id_prato, lanche.nome_prato, lanche.preco])
        for salgado in salgados:
            table_pratos.append([salgado.id_prato, salgado.nome_prato, salgado.preco])
        for pizza in pizzas:
            table_pratos.append([pizza.id_prato, pizza.nome_prato, pizza.preco])
        print(tabulate(table_pratos, headers=('ID Prato', 'Nome Prato', 'Preço')))
        self.menu_adm()
