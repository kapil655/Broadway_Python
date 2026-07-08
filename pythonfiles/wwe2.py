import requests
from wwe1 import send_message_to_viber


def get_wrestlers_images():
    url = "https://dummyjson.com/users"   

    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()["users"]

        for w in data:
                message = f"""
    Stage Name: {w['firstName']}
    Real Name: {w['lastName']}
    Age: {w['age']}
    Country: {w['address']['city']}
"""

        image = "https://i.imgur.com/1bX5QH6.png"

        send_message_to_viber(message, image)

     


get_wrestlers_images()




#https://documenter.getpostman.com/view/9564387/TzRPip7u#e35cdc70-42ac-474f-aad2-0172646527dd