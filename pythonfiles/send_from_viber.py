import importlib.util
import sqlite3
from pathlib import Path

module_path = Path(__file__).with_name("message.py")
spec = importlib.util.spec_from_file_location("message", module_path)
message = importlib.util.module_from_spec(spec)
spec.loader.exec_module(message)
send_message_to_viber = message.send_message_to_viber

conn = sqlite3.connect(r"D:\database\football.db")
cursor = conn.cursor()

cursor.execute("SELECT name, city, stadium, image FROM teams")
rows = cursor.fetchall()

for name, city, stadium, image in rows:

    message = f"{name} is based in {city}. Home stadium: {stadium}"

    send_message_to_viber(message, image)

conn.close()