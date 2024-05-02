from crypt import methods
from flask import Flask, redirect, render_template, request
from todo_app.data.trello_items import add_item, get_items, move_item_to_done

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = get_items()
    return render_template ('index.html', items = items)

@app.route('/add-todo', methods=["POST"])
def add_todo():
    new_todo_title = request.form.get('title')
    add_item(new_todo_title)
    return redirect('/')

@app.route('/complete-item/<todo_id>', methods=["POST"])
def complete_item (todo_id):
    move_item_to_done(todo_id)
    return redirect('/')