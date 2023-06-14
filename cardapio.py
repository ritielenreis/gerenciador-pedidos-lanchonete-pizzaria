class Cardapio:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def cardapio(self):
        print('\n', '='*20, 'CARDÁPIO VIRTUAL', '='*20, ' \n')
        print('Lanches \t[1] \nSalgados \t[2] \nPizzas   \t[3] \n')
        while True:
            escolha = int(input('O que você gostaria de pedir?'))
            if escolha == 1:
                self.lanches_cardapio()
                break
            elif escolha == 2:
                self.salgados_cardapio()
                break
            elif escolha == 3:
                self.menu_pizza()
                break
            else:
                print('Opção inválida')

    def lanches_cardapio(self):
        for lanche in self.repositorio.lanches():
            print(lanche)

    def salgados_cardapio(self):
        for salgado in self.repositorio.salgados():
            print(salgado)

    def pizzas_cardapio(self):
        for pizza in self.repositorio.pizzas():
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
