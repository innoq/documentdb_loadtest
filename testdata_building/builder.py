import random
from datetime import datetime, timedelta

from common.users import get_random_users

from testdata_building.util import (rand_number_of_articles_per_offer,
                                    rand_number_of_offers_for_day,
                                    rand_offer_begin_offset_in_min,
                                    rand_offer_duration_in_h, rand_price,
                                    rand_quantity, rand_string)


def create_article():
    return {
        "id": rand_string(),
        "name": rand_string(),
        "description": rand_string(),
        "price": rand_price(),
        "available_quantity": rand_quantity(),
    }

def create_articles_for_offer():
    return [create_article() for _ in range(rand_number_of_articles_per_offer())]

def create_offer(day: datetime):
    start = day + timedelta(minutes=rand_offer_begin_offset_in_min())
    end = start + timedelta(hours=rand_offer_duration_in_h())
    users = get_random_users(0.7)
    return {
        "title": rand_string(),
        "description": rand_string(),
        "starts": start,
        "ends": end,
        "articles": create_articles_for_offer(),
        "recipients": get_random_users(0.7)
    }

def create_random_number_of_offers(day: datetime):
    return [create_offer(day) for _ in range(rand_number_of_offers_for_day())]

def create_order(offer_id: str, article_id: str, user_id: str, time: datetime):
    return {
        "offer_id": offer_id,
        "article_id": article_id,
        "user_id": user_id,
        "time": time,
        "quantity": rand_quantity()
    }

def create_orders_for_offer_and_user(offer, user_id, time):
    return [create_order(offer["id"], article["id"], user_id, time) for article in offer["articles"]]

def create_orders_for_offer(offer, time):
    ordering_users = list(filter(lambda select: random.random() < 0.8, offer["recipients"]))
    orders = []
    for user_id in ordering_users:
        orders.extend(create_orders_for_offer_and_user(offer, user_id, time))
    return orders
