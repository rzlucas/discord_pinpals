# servers
from flask import current_app


class Servers:
    def __init__(self, ID=None, Name=None, OwnerID=None):
        self.ID = ID
        self.Name = Name
        self.OwnerID = OwnerID

    def serialize(self):
        return {
            "ID": self.ID,
            "Name": self.Name,
            "OwnerID": self.OwnerID
        }

    @classmethod
    def get(cls, server):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """SELECT ID, Name, OwnerID FROM Servers WHERE ID = %s"""
        params = server.ID,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """SELECT ID, Name, OwnerID FROM Servers"""
        results = DatabaseConnection.fetch_all(query)

        servers = []
        if results is not None:
            for result in results:
                servers.append(cls(*result))
        return servers

    @classmethod
    def create(cls, server):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """INSERT INTO Servers (Name, OwnerID) VALUES (%s, %s)"""
        params = server.Name, server.OwnerID
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, server):
        allowed_columns = {'Name', 'OwnerID'}
        query_parts = []
        params = []
        for key, value in server.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key}=%s")
                params.append(value)
        params.append(server.ID)

        DatabaseConnection = current_app.config['DatabaseConnection']
        query = "UPDATE Servers SET " + ", ".join(query_parts) + " WHERE ID=%s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, server):
        query = "DELETE FROM Servers WHERE ID=%s"
        params = server.ID,

        DatabaseConnection = current_app.config['DatabaseConnection']
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def search(cls, term, criteria="name"):
        DatabaseConnection = current_app.config['DatabaseConnection']

        if criteria == "name":
            query = """SELECT ID, Name, OwnerID FROM Servers WHERE Name LIKE %s"""
        # Si más adelante decides agregar la fecha de creación, puedes agregar un bloque elif aquí
        else:
            return []

        params = ("%" + term + "%",)
        results = DatabaseConnection.fetch_all(query, params=params)

        servers = []
        if results is not None:
            for result in results:
                servers.append(cls(*result))
        return servers
