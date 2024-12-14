import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='the_end_world',
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_results(self):
        return self.cursor.fetchall()

    def call_procedure(self, procedure_name, params=()):
        self.cursor.callproc(procedure_name, params)
        self.connection.commit()
        results = []
        for result in self.cursor.stored_results():
            results.extend(result.fetchall())
        return results

    def close(self):
        self.cursor.close()
        self.connection.close()
