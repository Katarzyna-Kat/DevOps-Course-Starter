from flask import Flask, render_template, request, redirect, url_for

# from todo_app.data.session_items import get_items, add_item
from todo_app.data.trello_items import (
    show_cards,
    add_item,
    delete_item,
    move_to_todo,
    move_to_progress,
    move_to_done,
)

from todo_app.flask_config import Config

from todo_app.class_items import Item


app = Flask(__name__)
app.config.from_object(Config())


# fetching


@app.route("/", methods=["GET"])
def index():
    all_items = show_cards()
    list_of_cards_todo = []
    list_of_cards_doing = []
    list_of_cards_done = []
    for list in all_items:
        for trellocard in list["cards"]:
            card = Item.from_trello_card(trellocard, list["name"])
            if list["name"] == "To Do":
                list_of_cards_todo.append(card)
            elif list["name"] == "Doing":
                list_of_cards_doing.append(card)
            elif list["name"] == "Done":
                list_of_cards_done.append(card)
    return render_template(
        "index.html",
        list_of_cards_todo=list_of_cards_todo,
        list_of_cards_doing=list_of_cards_doing,
        list_of_cards_done=list_of_cards_done,
    )


# create init function lines 27-39

# add item


@app.route("/add", methods=["POST"])
def add():
    newitem = request.form["name"]
    add_item(newitem)
    return redirect(url_for("index"))


# deleteing item from list


@app.route("/delete/<id>", methods=["POST"])
def delete(id):
    delete_item(id=request.form["Remove_id"])
    return redirect(url_for("index"))


# moving to todo


@app.route("/into_todo/<id>", methods=["POST"])
def move_todo(id):
    move_to_todo(id=request.form["ToDo_id"])
    return redirect(url_for("index"))


# moving to progress


@app.route("/into_progress/<id>", methods=["POST"])
def move_progress(id):
    move_to_progress(id=request.form["Progress_id"])
    return redirect(url_for("index"))


# moving to done


@app.route("/into_done/<id>", methods=["POST"])
def move_done(id):
    move_to_done(id=request.form["Done_id"])
    return redirect(url_for("index"))
