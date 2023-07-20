from servico_cliente import ServicoCliente
from servico_adm import ServicoAdm
from menu_cliente import MenuCliente


class MenuInicial:
    def __init__(self):
        self._servico_adm = ServicoAdm()
        self._servico_cliente = ServicoCliente()

    @property
    def servico_cliente(self):
        if self._servico_cliente is None:
            self._servico_cliente = ServicoCliente()
        else:
            return self._servico_cliente

    @property
    def servico_adm(self):
        if self._servico_adm is None:
            self._servico_adm = ServicoAdm()

        return self.servico_adm

    def iniciar(self):
        print('='*20, 'MENU INICIAL', '='*20)
        print('Cliente \t[1] \nFuncionário  \t[2]\n')
        while True:
            escolha = int(input('O que você gostaria de acessar?'))
            if escolha == 1:
                self.menu_cliente()
                break
            elif escolha == 2:
                esta_autorizado = self.login_adm()
                if esta_autorizado is True:
                    print('Acesso Permitido')
                break
            else:
                print('Opção inválida')

    def menu_cliente(self):
        print('\n', '=' * 20, 'CADASTRO DE CLIENTE', '=' * 20, ' \n')
        while True:
            escolha = int(input('Já tem cadastro na loja? \nSIM \t[1] \nNÃO  \t[2] \n'))
            if escolha == 1:
                id_cliente = self.validar_telefone()
                cardapio_cliente = MenuCliente(id_cliente)
                cardapio_cliente.cardapio()
                return id_cliente
            elif escolha == 2:
                id_cliente = self.criar_cliente()
                cardapio_cliente = MenuCliente(id_cliente)
                cardapio_cliente.cardapio()
                return id_cliente
            else:
                print('Opção inválida')

    def validar_telefone(self):
        while True:
            telefone = str(input('Qual o número do telemóvel cadastrado?'))
            cliente = self.servico_cliente.validar_cliente(telefone)
            if telefone == cliente.telefone:
                print(' já cadastrado!')
                break
            else:
                print('Número Inválido')
        return cliente.id_cliente

    def criar_cliente(self):
        nome = str(input('Nome:'))
        telefone = str(input('Telefone:'))
        id_cliente_criado = self.servico_cliente.criar_cliente(nome, telefone)
        cliente = self.servico_cliente.ler_cliente(id_cliente_criado)
        print(f' Cliente {cliente.nome_cliente}  ID {cliente.id_cliente}', end='')
        return cliente.id_cliente

    def login_adm(self):
        tentativas = 0
        while True:
            id_adm = int(input('Digite seu ID:'))
            senha = str(input('Senha:'))
            adm = self.servico_adm.validar_adm(id_adm, senha)
            print(adm.nome_adm)
            if adm is not None:
                print(f' Login autorizado para Funcionario {adm.nome_adm}  ID {adm.id_adm}')
                return True
            elif tentativas == 2:
                print('Numero de tentativas excedido!')
                return False
            else:
                tentativas += 1
                print('Senha Inválida')



    '''def validar_adm(self, id_adm, senha):
        while True:
            adm = self._servico_adm.validar_adm(id_adm, senha)
            if senha == adm.senha:
                print(f' Login autorizado para Funcionario {adm.nome_adm}  ID {adm.id_adm}')
                break
            else:
                print('Senha Inválida')
        return adm
'''