from flask import Flask, render_template, request, redirect, url_for

# from todo_app.data.session_items import get_items, add_item
from todo_app.data.trello_items import (
    show_cards,
    add_item,
    delete_item,
)

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


# fetching
@app.route("/", methods=["GET"])
def index():
    all_items = show_cards()
    list_of_cards = []
    for sections in all_items:
        for card in sections:
            list_of_cards.append(card)
            return render_template("index.html", list_of_items=list_of_cards)


# # adding to the list
# @app.route("/add", methods=["POST"])
# def add():
#     newitem = request.form["title"]
#     add_item(newitem)
#     return redirect(url_for("index"))


# deleteing item from list

# @app.route("/delete/<id>", methods=["POST"])
# def delete(id):
#     # ????????
#     # delete_item
#     return redirect(url_for("index"))
