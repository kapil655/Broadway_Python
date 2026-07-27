import requests
import mysql.connector
from beauty import send_message_to_viber

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python-jun-1"
)

cursor = db.cursor()


def get_brands():
    url = "https://www.api.foreveryng.com/api/getBrandList?source=website&device=website"
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        brands = data.get("data", {}).get("brands", [])

        query = """
        INSERT INTO product (
            id,
            title,
            slug,
            image
        ) VALUES (%s, %s, %s, %s)
        """

        for brand in brands:
            bid = brand.get("id")
            if bid:
                title = brand.get("title", "")
                slug = brand.get("slug", "")
                image = brand.get("image", "")

                cursor.execute(query, (bid, title, slug, image))
                db.commit()

                message = f"{title} ({slug})"
                send_message_to_viber(
                    bid, image, slug, title, message
                )
    else:
        print("API failed:", r.status_code, r.text)


get_brands()

cursor.close()
db.close()
