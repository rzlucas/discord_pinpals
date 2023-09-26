# auth_controller.py

from flask import request, jsonify, session
from ..models.users import Users
from werkzeug.security import generate_password_hash, check_password_hash


class AuthController:
    @classmethod
    def login(cls):
        data = request.json
        username = data.get('Username')
        password = data.get('Password')

        user = Users.get_by_username(username)

        if user:
            if check_password_hash(user.Password, password):
                session['user_id'] = user.ID
                return jsonify({"message": "Logged in successfully"}), 200
            else:
                print("Incorrect password for user:", username)
                return jsonify({"message": "Invalid username or password"}), 401
        else:
            print("User not found:", username)  # Add this line
            return jsonify({"message": "Invalid username or password"}), 401

    @classmethod
    def register(cls):
        data = request.json

        # Simplemente llama a generate_password_hash sin especificar el método
        hashed_password = generate_password_hash(data.get('Password'))

        new_user = Users(
            Username=data.get('Username'),
            Email=data.get('Email'),
            Password=hashed_password
        )
        Users.create(new_user)
        return jsonify({"message": "User registered successfully"}), 201

    @classmethod
    def logout(cls):
        session.pop('user_id', None)
        return jsonify({"message": "Logged out successfully"}), 200
