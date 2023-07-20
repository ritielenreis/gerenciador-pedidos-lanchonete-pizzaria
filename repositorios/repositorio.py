from mysql.connector import connect, Error


class Repositorio:
    def __init__(self):
        self.connection = connect(user='dono_lanchonete',
                         password='uma_senha_forte',
                         host='localhost',
                         database='lanchonete')

    def _executar_query(self, query):
        try:
            cursor = self.connection.cursor(buffered=True)
            cursor.execute(query)
            self.connection.commit()
        except Error as e:
            self.connection.rollback()
            print(f"[{self.__class__.__name__}] Error:", e)

    def _retornar_resultados(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"[{self.__class__.__name__}] Error:", e)

    def _retornar_resultado(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchone()
        except Error as e:
            print(f"[{self.__class__.__name__}] Error:", e)

    def deletar(self, table, nome_id, valor_id):
        query = f'DELETE FROM {table} WHERE {nome_id} = {valor_id};'
        self._executar_query(query)

        print(f'{table} {valor_id} apagado!')
