import requests
from project3 import send_message_to_viber
image_url = "https://scores.iplt20.com/ipl/teamlogos/CSK.png"
def send_message_to_vibe():
    url = "https://scores.iplt20.com/ipl/teamlogos/CSK.png"
    r = requests.get(url=url)
    if r.status_code == 200:
         result = r.json()['data']
         

# for image in range(1,10):
image = f"https://scores.iplt20.com/ipl/teamlogos/CSK.png"

send_message_to_viber("hello sir",image)



