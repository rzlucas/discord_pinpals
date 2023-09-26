# config.py
from dotenv import dotenv_values
import os


class Config:
    config = dotenv_values(".env")

    # Cargar SECRET_KEY desde una variable de entorno o usar una clave predeterminada
    SECRET_KEY = os.getenv('SECRET_KEY') or config.get('SECRET_KEY') or 'una_clave_secreta_predeterminada'

    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True

    DATABASE_USERNAME = config['DATABASE_USERNAME']
    DATABASE_PASSWORD = config['DATABASE_PASSWORD']
    DATABASE_HOST = config['DATABASE_HOST']
    DATABASE_PORT = config['DATABASE_PORT']
    DATABASE_NAME = config['DATABASE_NAME']

    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"
