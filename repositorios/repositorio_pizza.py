from .repositorio_prato import RepositorioPrato
from objetos.pizza import Pizza


class RepositorioPizza(RepositorioPrato):
    def __init__(self):
        super().__init__()

    def criar_pizza(self, nome_prato, preco, validade, peso, molho, recheio, borda):
        id_prato = self.criar_prato(nome_prato, preco, validade, peso)
        query = f"INSERT INTO pizza (id_prato, molho, recheio, borda) VALUES ({id_prato}, '{molho}', '{recheio}', '{borda}');"
        self._executar_query(query)
        query1 = f"SELECT pizza.id_prato FROM pizza JOIN prato on pizza.id_prato=prato.id_prato WHERE nome_prato = '{nome_prato}';"
        id_pizza = self._retornar_resultado(query1)

        if id_pizza == None:
            print(f"[{self.__class__.__name__}] Pizza nao encontrada.")
        print(f"[{self.__class__.__name__}] Pizza encontrada.")

        id_pizza = id_pizza[0]
        return id_pizza

    def ler_pizza(self, id_prato):
        query_pizza = f"""
                    SELECT pizza.id_prato, nome_prato, preco, validade, peso, molho, recheio, borda
                    FROM pizza
                    JOIN prato ON pizza.id_prato = prato.id_prato
                    WHERE pizza.id_prato = {id_prato};"""
        (id_prato, nome_prato, preco, validade, peso, molho, recheio, borda) = self._retornar_resultado(query_pizza)
        pizza = Pizza(id_prato, nome_prato, preco, validade, peso, molho, recheio, borda)
        return pizza

    def ler_pizzas(self):
        query_pizzas = """
            SELECT pizza.id_prato, nome_prato, preco, validade, peso, molho, recheio, borda
            FROM pizza
            JOIN prato
                ON pizza.id_prato = prato.id_prato            
        """
        resultados = self._retornar_resultados(query_pizzas)
        # Transformar os resultados em objetos
        pizzas = []
        for (id_prato, nome_prato, preco, validade, peso, molho, recheio, borda) in resultados:
            pizza = Pizza(id_prato, nome_prato, preco, validade, peso, molho, recheio, borda)
            pizzas.append(pizza)
            print(pizza)
        return pizzas