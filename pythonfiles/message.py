import requests
import json

token = "56c4977935f284d0-2473cf174906088-178254ed4f7db50c"
user_id = "lsPph8fpPvYKrEapzeQvBA=="
viber_url = "https://chatapi.viber.com/pa/post"

def send_message_to_viber(message, image_url):

    payload = {
        "auth_token": token,
        "from": user_id,
        "type": "picture",
        "text": message,
        "media": image_url,
        "thumbnail": image_url
    }

    r = requests.post(viber_url, data=json.dumps(payload))

    print("Status:", r.status_code, r.text)