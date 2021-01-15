from datetime import datetime

from common.mongodb_repo import (find_offer, find_offers,
                                 find_orders_by_offer_ids_and_user_id)

from loadtest.stopwatch import Stopwatch


def get_offers_list(user_id: str, time: datetime):
    sw = Stopwatch()
    offers = find_offers(user_id, time)
    offer_ids = [offer["id"] for offer in offers]
    find_orders_by_offer_ids_and_user_id(offer_ids, user_id)
    sw.measure("get_offers_list")
    return offers

def get_offer_details(offer_id: str, user_id: str):
    sw = Stopwatch()
    offer = find_offer(offer_id)
    orders = find_orders_by_offer_ids_and_user_id([offer_id], user_id)
    sw.measure("get_offer_details")
    return offer
