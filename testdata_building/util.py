import random

random.seed("a_seed")

CHARS = " ABCDEFGHIJKLMNOPQRST abcdefghijklmnopqrst "

def rand_char():
    i = random.randint(0, len(CHARS) - 1)
    return CHARS[i]

def rand_string():
    return "".join([rand_char() for _ in range(random.randint(5, 70))])

def rand_price():
    return round(random.random() * 100, 2)

def rand_quantity():
    return random.randint(10, 500)

def rand_offer_duration_in_h():
    return random.randint(8, 24 * 30)

def rand_offer_begin_offset_in_min():
    return random.randint(0, 120)

def rand_number_of_articles_per_offer():
    return random.randint(1, 40)

def rand_number_of_offers_for_day():
    return random.randint(10, 30)
