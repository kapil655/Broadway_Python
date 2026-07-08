import requests
import json

token = "56c4977935f284d0-2473cf174906088-178254ed4f7db50c"
user_id = "lsPph8fpPvYKrEapzeQvBA=="
viber_url = "https://chatapi.viber.com/pa/post"


def send_message_to_viber(message, image_url=None):
    payload = {
        "auth_token": token,
        "from": user_id,
        "type": "text" if not image_url else "picture",
        "text": message
    }

    if image_url:
        payload["media"] = image_url
        payload["thumbnail"] = image_url

    r = requests.post(viber_url, data=json.dumps(payload),
                      headers={"Content-Type": "application/json"})

    print(r.status_code, r.text)