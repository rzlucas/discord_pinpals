# messages
from flask import current_app


class Messages:
    def __init__(self, ID=None, Content=None, UserID=None, ChannelID=None):
        self.ID = ID
        self.Content = Content
        self.UserID = UserID
        self.ChannelID = ChannelID

    def serialize(self):
        return {
            "ID": self.ID,
            "Content": self.Content,
            "UserID": self.UserID,
            "ChannelID": self.ChannelID
        }

    @classmethod
    def get(cls, message):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """SELECT ID, Content, UserID, ChannelID FROM Messages WHERE ID = %s"""
        params = message.ID,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """SELECT ID, Content, UserID, ChannelID FROM Messages"""
        results = DatabaseConnection.fetch_all(query)

        messages = []
        if results is not None:
            for result in results:
                messages.append(cls(*result))
        return messages

    @classmethod
    def create(cls, message):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """INSERT INTO Messages (Content, UserID, ChannelID) VALUES (%s, %s, %s)"""
        params = message.Content, message.UserID, message.ChannelID
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, message):
        """Update a message"""
        allowed_columns = {'Content', 'UserID', 'ChannelID'}
        query_parts = []
        params = []
        for key, value in message.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key}=%s")
                params.append(value)
        params.append(message.ID)

        DatabaseConnection = current_app.config['DatabaseConnection']
        query = "UPDATE Messages SET " + ", ".join(query_parts) + " WHERE ID=%s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, message):
        """Delete a message"""
        query = "DELETE FROM Messages WHERE ID=%s"
        params = message.ID,

        DatabaseConnection = current_app.config['DatabaseConnection']
        DatabaseConnection.execute_query(query, params=params)
