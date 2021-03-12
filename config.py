from pymongo import MongoClient
import urllib.parse


def configure_db():
    username = "jokeuser"
    password = "jokeuser-2021"
    db_name = "jokedb"
    host = "192.168.90.232"
    port = 27017
    client = MongoClient(f'mongodb://{username}:{urllib.parse.quote_plus(password)}@{host}:{port}/{db_name}')
    db = client['jokedb']
    return db
