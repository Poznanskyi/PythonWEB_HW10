from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb+srv://poz:bN342Po12@firstcluster.dxzj24g.mongodb.net/test")

    db = client.hw10
    return db