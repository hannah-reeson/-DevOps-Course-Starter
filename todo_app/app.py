from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import *


app = Flask(__name__)
app.config.from_object(Config)
 

@app.route('/', methods=['GET'])
def index():
    items = get_items()
    return render_template('index.html', items = items)

@app.route('/', methods=['POST'])
def addItems():
    add_item(request.form.get('title'))
    return redirect("/")
    

   

if __name__ == '__main__':
    app.run()
