from flask_login import UserMixin

from db import get_db


class User(UserMixin):
    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.email = email

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.get_collection('Users').find_one({"_id": user_id})
        if not user:
            return None

        user = User(id_=user['_id'], name=user['name'], email=user['email'])
        return user

    @staticmethod
    def create(id_, name, email):
        db = get_db()
        db.get_collection('Users').insert_one({"_id": id_, "name": name, "email": email})
