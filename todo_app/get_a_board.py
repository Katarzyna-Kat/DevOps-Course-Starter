import requests
import dotenv
import os

dotenv.load_dotenv("../.env")

ID = os.getenv("KAT_BOARD_ID")
KEY = os.getenv("KAT_KEY")
TOKEN = os.getenv("KAT_TOKEN")


url = f"https://api.trello.com/1/boards/{ID}?key={KEY}&token={TOKEN}&cards=open"

response = requests.get(url)
print(response.text)