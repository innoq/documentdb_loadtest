from datetime import datetime
from typing import List

from bson.objectid import ObjectId
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
from loadtest.stopwatch import Stopwatch
from pymongo import MongoClient

try:
    _client = MongoClient(host=DB_HOST, port=DB_PORT, username=DB_USER, password=DB_PASSWORD)
    _db = _client.get_database(DB_NAME)

    _offers = _db.get_collection("offers")
    _orders = _db.get_collection("orders")
    print("database connection established")
except:
    print(f"failed to establish database connection to {DB_HOST}:{DB_PORT}")


def drop_db():
    _client.drop_database(DB_NAME)

def insert_one_offer(offer):
    res = _offers.insert_one(offer)
    return {"id": str(res.inserted_id), **offer}

def insert_many_orders(orders):
    _orders.insert_many(orders)

def find_offers(user_id: str, time: datetime):
    sw = Stopwatch()
    offers = list(_offers.find({
        "starts": {"$lt": time}, 
        "ends": {"$gt": time}, 
        "recipients": user_id
    }))
    sw.measure("find_offers")
    return [{"id": str(offer["_id"]), **offer} for offer in offers]

def find_offer(offer_id: str):
    sw = Stopwatch()
    offer = _offers.find_one({"_id": ObjectId(offer_id)})
    sw.measure("find_offer")
    return offer

def find_orders_by_offer_ids_and_user_id(offer_ids: List[str], user_id: str):
    sw = Stopwatch()
    orders = list(_orders.find({
        "offer_id": {"$in": offer_ids},
        "user_id": user_id
    }))
    sw.measure("find_orders_by_offer_ids_in_and_user_id")
    return orders

def find_orders_by_offer_id_and_user_id(offer_id: str, user_id: str):
    sw = Stopwatch()
    orders = list(_orders.find({
        "offer_id": offer_id,
        "user_id": user_id
    }))
    sw.measure("find_orders_by_offer_id_and_user_id")
    return orders

def create_indices():
    _offers.create_index("recipients")
    _offers.create_index("starts")
    _offers.create_index("ends")
    _orders.create_index("offer_id")
    _orders.create_index("user_id")
