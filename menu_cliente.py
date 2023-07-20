from servico_cliente import ServicoCliente
from nota_fiscal import NotaFiscal


class MenuCliente:
    def __init__(self, id_cliente):
        self.servico = ServicoCliente()
        self.id_cliente = id_cliente
        self._id_pedido = None

    def id_pedido(self):
        if self._id_pedido is None:
            self._id_pedido = self.servico.criar_pedido(self.id_cliente)

        return self._id_pedido

    def cardapio(self):
        print('\n', '='*20, 'CARDÁPIO VIRTUAL', '='*20, ' \n')
        print('Lanches \t[1] \nSalgados \t[2] \nPizzas   \t[3] \nVer Pedido   \t[4] \n')
        while True:
            escolha = int(input('O que você gostaria de pedir?'))
            if escolha == 1:
                self.lanches_cardapio()
                self.menu_rodape()
                break
            elif escolha == 2:
                self.salgados_cardapio()
                self.menu_rodape()
                break
            elif escolha == 3:
                self.menu_pizza()
                self.menu_rodape()
                break
            elif escolha == 4:
                self.ver_pedido(self.id_pedido())
                self.menu_rodape()
                break
            else:
                print('Opção inválida')


    def ver_pedido(self, id_pedido):
        pedido = NotaFiscal()
        ver_pedido = pedido.ver_info_pedido(id_pedido)
        return ver_pedido

    def pagamento(self):
        print('\033[7:33mDirija-se ao caixa para efetuar o pagamento do seu pedido.\033[0m')

    def lanches_cardapio(self):
        for lanche in self.servico.ler_lanches():
            print(lanche)

    def salgados_cardapio(self):
        for salgado in self.servico.ler_salgados():
            print(salgado)

    def pizzas_cardapio(self):
        for pizza in self.servico.ler_pizzas():
            print(pizza)

    def menu_pizza(self):
        while True:
            print('\nMonte sua Pizza          \t[1]\nPizzas prontas          \t[2]\nVoltar ao menu principal   \t[0]\n')
            escolha = int(input('O que você gostaria de pedir?'))
            if escolha == 1:
                self.monte_pizza()
                break
            elif escolha == 2:
                self.pizzas_cardapio()
                break
            elif escolha == 0:
                self.cardapio()
                break
            else:
                print('Opção inválida')

    def monte_pizza(self):
        print('\n', '>'*20, 'Opção ainda indisponivel no menu!', '<'*20)
        self.cardapio()

    def menu_rodape(self):
        print('\n', '='*20, 'OPÇÕES', '='*20, ' \n')
        print('Adicionar item ao pedido \t[1] \nConcluir pedido \t[2] \nVoltar Menu \t[3] \nCancelar  \t[4] \n')
        while True:
            escolha = int(input('Escolha a opção desejada: '))
            if escolha == 1:
                self.add_itens(self.id_pedido())
                break
            elif escolha == 2:
                self.pagamento()
                break
            elif escolha == 3:
                self.cardapio()
                break
            elif escolha == 4:
                print('Pedido Cancelado!')
                break
            else:
                print('Opção inválida')

    def add_itens(self, id_pedido=None):
        escolha = int(input('O que você gostaria de pedir? [Digite o número do prato escolhido]'))
        quantidade = int(input('Qual a quantidade?'))

        self.servico.add_item_pedido(id_pedido, escolha, quantidade)
        self.menu_rodape()
