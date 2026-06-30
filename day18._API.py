import requests
from project1 import send_message_viber
# for activating scripts 
 #.\python_broadway\Scripts\activate    



def premier_league_teams():
    url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/teams?_limit=60"

    r = requests.get(url=url)

    if r.status_code == 200:
        response = r.json()
        print(response.keys())

        result = response['data']
        final_data= result

        for i in final_data:
           result = print(f"the club name is {i['name']} and it's abbreviation is {i['abbr']} .")

        send_message_viber(result)

        print(r)

