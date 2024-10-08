import os
from flask import Flask, redirect, render_template, request
from todo_app.data.mongo_entries import add_item, get_items, move_item_to_done

from todo_app.data.view_model import ViewModel

from todo_app.flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    app.logger.setLevel(os.environ.get('LOG_LEVEL'))
    
    @app.route('/')
    def index():
        items = get_items()
        view_model = ViewModel(items)
        app.logger.info("Homepage accessed")
        return render_template ('index.html', view_model = view_model)

    @app.route('/add-todo', methods=["POST"])
    def add_todo():
        new_todo_title = request.form.get('title')
        add_item(new_todo_title)
        app.logger.info("Added a new todo item {new_todo_title}")
        return redirect('/')

    @app.route('/complete-item/<todo_id>', methods=["POST"])
    def complete_item (todo_id):
        move_item_to_done(todo_id)
        app.logger.info("Moved item to complete {todo_id}")
        return redirect('/')

    return app