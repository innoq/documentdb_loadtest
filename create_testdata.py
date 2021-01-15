from datetime import datetime, timedelta

from common.mongodb_repo import (create_indices, drop_db, insert_many_orders,
                                 insert_one_offer)
from testdata_building.builder import (create_orders_for_offer,
                                       create_random_number_of_offers)

N_DAYS = 60
TODAY = datetime.now().replace(hour=6, minute=0, second=0)

drop_db()

for d in range(N_DAYS):
    day = TODAY - timedelta(days=(N_DAYS - d))
    print("inserting data for day " + day.isoformat())
    offers = [insert_one_offer(offer) for offer in create_random_number_of_offers(day)]
    [insert_many_orders(create_orders_for_offer(offer, day)) for offer in offers]

print("creating indices...")
create_indices()
