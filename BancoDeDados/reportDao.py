from flask import flash, redirect, url_for
import connection

connection = connection.create_server_connection('localhost', 'root', connection.pw)

class Report():
    def salvarNovo(self, corPin: int, endereco_id: int, usuario_id: int):
        insert_report_query = """
        INSERT INTO report (situacao, endereco_id) 
        VALUES (%s, %s)
        """
        cursor = connection.cursor()
        cursor.execute(insert_report_query, (corPin, endereco_id))
        connection.commit()
        cursor.close()
        report_id = cursor.lastrowid  # Pega o ID do report recém-criado
        self._saveUsuarioReport(report_id, usuario_id)


    def _saveUsuarioReport(self, report_id: int, usuario_id: int):
        # Inserindo na tabela de relacionamento usuario_report
        insert_usuario_report_query = """
            INSERT INTO usuario_report (usuario_id, report_id) 
            VALUES (%s, %s)
        """
        cursor = connection.cursor()
        cursor.execute(insert_usuario_report_query, (usuario_id, report_id))
        
        connection.commit()
        cursor.close()
