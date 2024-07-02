from flask import session

from src.classes.database.DatabaseController import DatabaseController

class SessionController:
    @staticmethod
    def is_authenticated(self):
        return session[""]