from flask import Flask, render_template
from todo_app.data.session_items import get_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    #return 'Hello World!!!!'
    items = get_items()
    return render_template ('index.html', todo_items = items)
