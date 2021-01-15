from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
from pymongo import MongoClient

_client = MongoClient(host=DB_HOST, port=DB_PORT, username=DB_USER, password=DB_PASSWORD)
_db = _client.get_database(DB_NAME)

_offers = _db.get_collection("offers")
_orders = _db.get_collection("orders")

def drop_db():
    _client.drop_database(DB_NAME)

def insert_one_offer(offer):
    res = _offers.insert_one(offer)
    return {"id": str(res.inserted_id), **offer}

def insert_many_orders(orders):
    _orders.insert_many(orders)

def create_indices():
    _offers.create_index("recipients")
    _offers.create_index("starts")
    _offers.create_index("ends")
    _orders.create_index("offer_id")
    _orders.create_index("user_id")
