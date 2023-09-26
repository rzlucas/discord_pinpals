# channel
from flask import current_app


class Channels:
    def __init__(self, ID=None, Name=None, ServerID=None):
        self.ID = ID
        self.Name = Name
        self.ServerID = ServerID

    def serialize(self):
        return {
            "ID": self.ID,
            "Name": self.Name,
            "ServerID": self.ServerID
        }

    @classmethod
    def get(cls, channel_id):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """SELECT ID, Name, ServerID FROM Channels WHERE ID = %s"""
        params = channel_id.ID,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """SELECT ID, Name, ServerID FROM Channels"""
        results = DatabaseConnection.fetch_all(query)

        channels = []
        if results is not None:
            for result in results:
                channels.append(cls(*result))
        return channels

    @classmethod
    def create(cls, channel):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """INSERT INTO Channels (Name, ServerID) VALUES (%s, %s)"""
        params = channel.Name, channel.ServerID
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, channel):
        """Update a channel"""
        allowed_columns = {'Name', 'ServerID'}
        query_parts = []
        params = []
        for key, value in channel.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key}=%s")
                params.append(value)
        params.append(channel.ID)

        DatabaseConnection = current_app.config['DatabaseConnection']
        query = "UPDATE Channels SET " + ", ".join(query_parts) + " WHERE ID=%s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, channel):
        """Delete a channel"""
        query = "DELETE FROM Channels WHERE ID=%s"
        params = channel.ID,

        DatabaseConnection = current_app.config['DatabaseConnection']
        DatabaseConnection.execute_query(query, params=params)
