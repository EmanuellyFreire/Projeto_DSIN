from BancoDeDados import connection

newConnection = connection.create_server_connection('localhost', 'root', connection.pw)

class endereco():
    def salvarNovo(self, rua: str, cidade: str, nmr: str, comp: str):
        insert_endereco_query = """
        INSERT INTO banco.endereco (rua, cidade, numero, complemento) 
        VALUES (%s, %s, %s, %s)
        """
        cursor = newConnection.cursor()
        cursor.execute(insert_endereco_query, (rua, cidade, nmr, comp))
        return cursor.lastrowid  # Pega o ID do endereço recém-criado