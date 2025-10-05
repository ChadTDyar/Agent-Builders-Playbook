import requests

def send_slack_notification(webhook_url, message):
    payload = {"text": message}
    resp = requests.post(webhook_url, json=payload)
    return resp.status_code == 200
