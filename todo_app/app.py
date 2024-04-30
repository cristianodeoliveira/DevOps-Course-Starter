from crypt import methods
from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, get_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    #return 'Hello World!!!!'
    items = get_items()
    return render_template ('index.html', items = items)

@app.route('/add-todo', methods=["POST"])
def add_todo():
    new_todo_title = request.form.get('title')
    add_item(new_todo_title)
    return redirect('/')