import requests
import json

token = "56c4977935f284d0-2473cf174906088-178254ed4f7db50c"
user_id = "lsPph8fpPvYKrEapzeQvBA=="
viber_url = "https://chatapi.viber.com/pa/post"

payload = {
    "auth_token":token,
    "from":user_id,
    "type":"text",
    "text":"this is test"
}

payload_image = {
    "auth_token":token,
    "from":user_id,
    "type":"picture",
    "text":"this is test",
    "media":"https://www.images.com/img.jpg",
    "thumbnail":"https://www.images.com/thumb.jpg"
}

def send_message_to_viber(message,pic):
    payload_image['text']=message
    payload_image['media']=pic
    payload_image['thumbnail']=pic

    r = requests.post(url=viber_url, data=json.dumps(payload_image))
    print(r)