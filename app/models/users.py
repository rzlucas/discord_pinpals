# users
from flask import current_app, jsonify, session, redirect
from sqlalchemy.testing.suite.test_reflection import users
from werkzeug.security import check_password_hash


class Users:
    def __init__(self, ID=None, Username=None, Email=None, Password=None, ProfilePicture=None):
        self.ID = ID
        self.Username = Username
        self.Email = Email
        self.Password = Password
        self.ProfilePicture = ProfilePicture

    def serialize(self):
        return {
            "ID": self.ID,
            "Username": self.Username,
            "Email": self.Email,
            "ProfilePicture": str(self.ProfilePicture)
        }

    def check_password(self, password):
        return check_password_hash(self.Password, password)

    @classmethod
    def get(cls, user):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """SELECT ID, Username, Email, Password, ProfilePicture FROM Users WHERE ID = %s"""
        params = user.ID,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        return None

    @classmethod
    def get_all(cls):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """SELECT ID, Username, Email, Password, ProfilePicture FROM Users"""
        results = DatabaseConnection.fetch_all(query)

        users = []
        if results is not None:
            for result in results:
                users.append(cls(*result))
        return users

    @classmethod
    def create(cls, user):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """INSERT INTO Users (Username, Email, Password, ProfilePicture) VALUES (%s, %s, %s, %s)"""
        params = user.Username, user.Email, user.Password, user.ProfilePicture
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, user):
        """Update a user"""
        allowed_columns = {'Username', 'Email', 'Password', 'ProfilePicture'}
        query_parts = []
        params = []
        for key, value in user.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key}=%s")
                params.append(value)
        params.append(user.ID)

        DatabaseConnection = current_app.config['DatabaseConnection']
        query = "UPDATE Users SET " + ", ".join(query_parts) + " WHERE ID=%s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, user):
        """Delete a user"""
        query = "DELETE FROM Users WHERE ID=%s"
        params = user.ID,

        DatabaseConnection = current_app.config['DatabaseConnection']
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get_by_username(cls, username):
        DatabaseConnection = current_app.config['DatabaseConnection']
        query = """SELECT ID, Username, Email, Password, ProfilePicture FROM Users WHERE Username = %s"""
        params = (username,)
        result = DatabaseConnection.fetch_one(query, params=params)
        if result:
            return cls(*result)
        return None


def login(username, password):
    user = users.get(username)

    if user is None:
        return jsonify({'success': False, 'error': 'El usuario no existe'})

    if not user.check_password(password):
        return jsonify({'success': False, 'error': 'La contraseña es incorrecta'})

    session['username'] = user.username
    session['id'] = user.id

    return redirect('/profile')
