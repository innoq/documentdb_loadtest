import concurrent.futures
import random
from datetime import datetime, timedelta

import boto3

from common.aws_s3_uploader import upload_file
from common.slack_webhook import send_data_to_slack
from common.users import get_random_user_id
from config import DURATION, N_THREADS, S3_BUCKET_NAME, SLACK_WEBHOOK_URL
from loadtest.offer_service import get_offer_details, get_offers_list
from loadtest.stopwatch import Stopwatch

TODAY = datetime.now()
MAX_HOURS_IN_PAST = 24 * 60

def simulate_user_action():
    time = TODAY - timedelta(hours=random.randint(0, MAX_HOURS_IN_PAST))
    user_id = get_random_user_id()
    offer_list = get_offers_list(user_id, time)
    if len(offer_list) < 2:
        return
    interesting_offers = list(filter(lambda o: random.random() < 0.2, offer_list))
    [get_offer_details(offer["id"], user_id) for offer in interesting_offers]

def run_thread(thread_name):
    test_end = datetime.now() + timedelta(seconds=DURATION)
    while datetime.now() < test_end:
        simulate_user_action()

print(f"load testing the database with {N_THREADS} threads for {DURATION}s")

with concurrent.futures.ThreadPoolExecutor(max_workers=N_THREADS) as executor:
        executor.map(run_thread, range(N_THREADS))

Stopwatch.print_report()

if S3_BUCKET_NAME:
    file_name = f"loadtest_results_{N_THREADS}_threads_for_{DURATION}s_on_{datetime.now().isoformat()}.txt"
    Stopwatch.save_report(file_name)
    upload_file(file_name, file_name)

if SLACK_WEBHOOK_URL:
    send_data_to_slack(Stopwatch.get_formatted_report())

print("done")
