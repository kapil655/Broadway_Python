import requests
from final_project import send_message_to_viber

img1="https://scores.iplt20.com/ipl/teamlogos/CSK.png"

img2="https://a.espncdn.com/photo/2024/0714/240715_top-100_inlines_013.jpg"

img3="https://upload.wikimedia.org/wikipedia/en/2/2e/Mumbai_Indians_Logo.svg"

def send_message_to_vibe():

    url = img1,img2,img3

    r = requests.get(url)

    if r.status_code == 200:

        print("Image is available.")


images = [
    img1,

    img2,

    img3

]


for image in images:

    send_message_to_viber("hello sir", image)