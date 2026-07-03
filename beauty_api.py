# import requests
# from beauty import send_message_to_viber

# brand_slug = []
# brand_image = []
# def get_brands():
#     url = "https://www.api.foreveryng.com/api/getBrandList?source=website&device=website"

#     r = requests.get(url)

#     if r.status_code == 200:
#         brands = r.json()["data"]["brands"]

#         brand_slug = []
#         brand_image = []

#         for item in brands:
#             brand_slug.append(item["slug"])
#             brand_image.append(item["image"])

#         print("Slugs:", brand_slug)
#         print("Images:", brand_image)

#     else:
#         print("Request failed:", r.status_code)

# get_brands()





import requests
from beauty import send_message_to_viber


def get_brands():
    url = "https://www.api.foreveryng.com/api/getBrandList?source=website&device=website"

    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()

        brands = data.get("data", {}).get("brands", [])

        for brand in brands:

            title = brand.get("title", "")
            slug = brand.get("slug", "")
            image = brand.get("image", "")

            message = f"{title} ({slug})"

           
            send_message_to_viber(image, slug, title, message)

    else:
        print("API failed:", r.status_code, r.text)


get_brands()