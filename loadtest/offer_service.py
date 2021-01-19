from datetime import datetime

from common.mongodb_repo import (find_offer, find_offers,
                                 find_orders_by_offer_ids_and_user_id_in)

from loadtest.stopwatch import Stopwatch


def get_offers_list(user_id_in: str, time: datetime):
    sw = Stopwatch()
    offers = find_offers(user_id_in, time)
    offer_ids = [offer["id"] for offer in offers]
    find_orders_by_offer_ids_and_user_id_in(offer_ids, user_id_in)
    sw.measure("get_offers_list")
    return offers

def get_offer_details(offer_id: str, user_id: str):
    sw = Stopwatch()
    offer = find_offer(offer_id)
    orders = find_orders_by_offer_ids_and_user_id_in([offer_id], user_id)
    sw.measure("get_offer_details")
    return offer
