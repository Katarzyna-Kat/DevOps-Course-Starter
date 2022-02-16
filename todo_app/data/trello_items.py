import requests
import os

BOARD_ID = os.getenv("KAT_BOARD_ID")
KEY = os.getenv("KAT_KEY")
TOKEN = os.getenv("KAT_TOKEN")
LIST_TODO = os.getenv("TODO_LIST_ID")
LIST_DOING = os.getenv("DOING_LIST_ID")
LIST_DONE = os.getenv("DONE_LIST_ID")


def show_cards():
    url = f"https://api.trello.com/1/boards/{BOARD_ID}/lists"

    query = {"key": KEY, "token": TOKEN, "cards": "open"}
    return requests.get(url, data=query).json()


def add_item(name):
    url = "https://api.trello.com/1/card?idList={LIST_TODO}&key={KEY}&token={TOKEN}&name={name}"

    query = {"idList": LIST_TODO, "key": KEY, "token": TOKEN, "name": name}
    return requests.request("POST", url, data=query)


def delete_item(id):
    url = f"https://api.trello.com/1/cards/{id}?key={KEY}&token={TOKEN}"

    query = {"id": id, "key": KEY, "token": TOKEN}
    return requests.delete(url=url, data=query)


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
