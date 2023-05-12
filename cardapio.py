from repositorio import Repositorio

def cardapio():
    print('\n','='*20, 'CARDÁPIO VIRTUAL', '='*20, ' \n')
    print('Lanches \t[1] \nSalgados \t[2] \nPizzas   \t[3] \n')
    while True:
        escolha = int(input('O que você gostaria de pedir?'))
        if escolha == 1:
            lanches_cardapio()
            break
        elif escolha == 2:
            salgados_cardapio()
            break
        elif escolha == 3:
            menu_pizza()
            break
        else:
            print('Opção inválida')


def lanches_cardapio():
    for lanche in repositorio.lanches():
        print(lanche)


def salgados_cardapio():
    for salgado in repositorio.salgados():
        print(salgado)


def pizzas_cardapio():
    for pizza in repositorio.pizzas():
        print(pizza)

def menu_pizza():
    while True:
        print('\nMonte sua Pizza          \t[1]\nPizzas prontas          \t[2]\nVoltar ao menu principal   \t[0]\n')
        escolha = int(input('O que você gostaria de pedir?'))
        if escolha == 1:
            monte_pizza()
            break
        elif escolha == 2:
            pizzas_cardapio()
            break
        elif escolha == 0:
            cardapio()
            break
        else:
            print('Opção inválida')

def monte_pizza():
    print('\n','>'*20,'Opção ainda indisponivel no menu!', '<'*20)
    cardapio()

repositorio = Repositorio()
cardapio()



