# create a class

import requests
import dotenv
import os
import json

from todo_app.class_items import Item

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
    all_items = requests.get(url, data=query).json()
    all_cards = []
    for list in all_items:
        for trellocard in list["cards"]:
            card = Item.from_trello_card(trellocard, list["name"])
            all_cards.append(card)
    return all_cards




##### Add function


def add_item(name):
    url = "https://api.trello.com/1/card?idList={LIST_TODO}&key={KEY}&token={TOKEN}&name={name}"

    query = {"idList": LIST_TODO, "key": KEY, "token": TOKEN, "name": name}
    return requests.request("POST", url, data=query)


##### Delete function


def delete_item(id):
    url = f"https://api.trello.com/1/cards/{id}?key={KEY}&token={TOKEN}"

    query = {"id": id, "key": KEY, "token": TOKEN}
    return requests.delete(url=url, data=query)


##### Update function


def move_to_todo(id):
    url = f"https://api.trello.com/1/cards/{id}?idList={LIST_TODO}&key={KEY}&token={TOKEN}"
    headers = {"Accept": "application/json"}

    return requests.request("PUT", url=url, data=headers)


def move_to_progress(id):
    url = f"https://api.trello.com/1/cards/{id}?idList={LIST_DOING}&key={KEY}&token={TOKEN}"
    headers = {"Accept": "application/json"}

    return requests.request("PUT", url=url, data=headers)


def move_to_done(id):
    url = f"https://api.trello.com/1/cards/{id}?idList={LIST_DONE}&key={KEY}&token={TOKEN}"
    headers = {"Accept": "application/json"}

    return requests.request("PUT", url=url, data=headers)
