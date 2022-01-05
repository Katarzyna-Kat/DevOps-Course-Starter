# create functions in here for the fetching of each list
# so I need to add update and delete buttons in the html

import requests
import dotenv
import os
import json

dotenv.load_dotenv("../.env")

BOARD_ID = os.getenv("KAT_BOARD_ID")
KEY = os.getenv("KAT_KEY")
TOKEN = os.getenv("KAT_TOKEN")
LIST_TODO = os.getenv("TODO_LIST_ID")
LIST_DOING = os.getenv("DOING_LIST_ID")
LIST_DONE = os.getenv("DONE_LIST_ID")


##### Fetch functions


def show_cards():
    url = f"https://api.trello.com/1/boards/{BOARD_ID}/lists"

    query = {"key": KEY, "token": TOKEN, "cards": "open"}
    return requests.get(url, data=query).json()


##### Add function


def add_item(name):
    url = "https://api.trello.com/1/card?idList={LIST_TODO}&key={KEY}&token={TOKEN}&name={name}"

    query = {"idList": LIST_TODO, "key": KEY, "token": TOKEN, "name": name}
    return requests.request("POST", url, data=query)


# ##### Delete function

# def delete_item(id):
#     url = f"https://api.trello.com/1/cards/{ID}?key={KEY}&token={TOKEN}"
#     headers = {"Accept": "application/json"}
#     response = requests.request("DELETE", url, headers=headers)


##### Update function

# def update_item():
