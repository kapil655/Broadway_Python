import requests
import json

token = "56c4977935f284d0-2473cf174906088-178254ed4f7db50c"

user_id = "lsPph8fpPvYKrEapzeQvBA=="

viber_url = "https://chatapi.viber.com/pa/post"

payload={
    
    "auth_token":token,
    
    "from":user_id,
    
    "type":"text",
    
    "text":"this is beauty product images"
    }

payload_img = {
    
    "auth_token":token,
    
    "from":user_id,
    
    "type":"picture",
    
    "text":"this is testing of beauty product",
    
    "media":"https://d2wfc4v12a2zxr.cloudfront.net/resized/medium/products/main_aqualogica-radiance-dewy-sunscreen-50gm_1778838011.webp"
}


def send_message_to_viber(image_url,slug,title,message  ):

    payload = {
        
        
        "auth_token": token,
        
        "from": user_id,
        
        "type": "picture",
        
        "text": message,
        
        "media": image_url,
        
        "title": title,
        
        "slug_image":slug
        
    }

    r = requests.post(viber_url, data=json.dumps(payload))

    print(slug, r.status_code, r.text)