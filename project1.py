import requests
import json

token = "56c4977935f284d0-2473cf174906088-178254ed4f7db50c"
user_id = "lsPph8fpPvYKrEapzeQvBA=="
viber_url = "https://chatapi.viber.com/pa/post"



payload={
     
"auth_token":token,
"from":user_id,
"type":"text",
"text":"this is test"


}


def send_message_viber(mmessgae=""):
    payload['text'] = mmessgae

    r =requests.post(url=viber_url,data=json.dumps(payload)) 

    print(r)

send_message_viber()


url = "https://markets.onlinekhabar.com/smtm/stock_live/sector-performance"
r = requests.get(url=url)

if r.status_code == 200:
            data = r.json()
            response = data['response']

            positive = []
            negative = []

            for item in response:
                if item['points_change'] < 0:
                    send_message_viber(f"{item['indices']} - ve")

                    negative.append(item['indices'])
                else:
                    send_message_viber(f"{item['indices']} + ve")

                    positive.append(item['indices'])

                

            print("positive------------>", len(positive))
            print("negative------------>", len(negative))




