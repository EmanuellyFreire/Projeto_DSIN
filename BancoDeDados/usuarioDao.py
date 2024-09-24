from flask import flash, redirect, url_for
import connection

connection = connection.create_server_connection('localhost', 'root', connection.pw)

class Usuario():
    def salvarNovo(self, usuario: str, senha: str):
        cursor = connection.cursor()
        # Verifica se o usuário já existe no banco
        result = self._verificarSeUserExist(usuario)

        if result:
            flash("Nome de usuário já existe!")
            return redirect(url_for("cadastro"))
        
        # Insere o novo usuário
        insert_query = "INSERT INTO usuario (login, senha) VALUES (%s, %s)"
        cursor.execute(insert_query, (usuario, senha))
        connection.commit()
        cursor.close()
    
    def _verificarSeUserExist(self, usuario: str):
        query = "SELECT * FROM usuario WHERE login = %s"
        cursor = connection.cursor()
        cursor.execute(query, (usuario,))
        return cursor.fetchone()
    
    def verificaLogin(self, usuario_login: str, senha_login: str):
        query = "SELECT * FROM usuario WHERE login = %s AND senha = %s"
        cursor = connection.cursor()
        cursor.execute(query, (usuario_login, senha_login))
        result = cursor.fetchone()
        cursor.close()
        return result

    
