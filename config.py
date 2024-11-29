import os

BASE_DIRECTORY = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///todo_board.db'

SECRET_KEY = "todoboard"