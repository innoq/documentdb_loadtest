import json

import requests
from config import SLACK_WEBHOOK_URL


def send_data_to_slack(data):
    print("posting data to slack")
    payload = {"text": data}
    res = requests.post(SLACK_WEBHOOK_URL, json.dumps(payload), headers={"Content-Type": "application/json"})
    if res.status_code != 200:
        print("ERROR posting data to slack")
        print(res.text)

