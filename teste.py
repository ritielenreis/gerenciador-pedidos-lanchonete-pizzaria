from menu_inicial import MenuInicial
from menu_adm import MenuADM
from repositorios import RepositorioAdm
from servico_adm import ServicoAdm

menu = MenuADM()
menu.menu_adm()
'''

menu = MenuInicial()
menu.iniciar()
rep = RepositorioAdm()
print(rep.validar_adm(0, '#3391Adm'))



menu.menu_cliente()

menu.list_pedidos()

serv = ServicoAdm()
print(serv.ler_cliente(39))


'''