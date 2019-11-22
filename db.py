from pymongo import MongoClient


def get_db():
    client = MongoClient(host='192.168.0.124', port=27017)

    db = client['GoogleLogin']

    return db
