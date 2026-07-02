import requests
from project1 import send_message_to_viber
image_url = "https://resources.premierleague.com/premierleague25/badges-alt/19.svg"
def get_images_using_api():
    url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/teams?_limit=60"
    r = requests.get(url=url)
    if r.status_code == 200:
        result = r.json()['data']
        for i in result:
            response = f"{i['name']} ({i['abbr']}) is a football club based in {i['stadium']['city']}. The team plays its home matches at  {i['stadium']['name']} and has participated in {len(i['seasons'])} recorded seasons."
            image = f"https://resources.premierleague.com/premierleague25/badges-alt/{i['id']}.svg"
            send_message_to_viber(response,image)



get_images_using_api()
