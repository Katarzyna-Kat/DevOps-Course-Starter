from flask import Flask, render_template, request
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

#getting the list
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', get_items = get_items)


#adding the list
@app.route('/add', methods=["POST"])
def add():
    newitem = request.form['title']
    add_item(newitem)
    return render_template('index.html')