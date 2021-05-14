from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import addCard, getLists, getCards, moveCard, removeCard

app = Flask(__name__)
app.config.from_object(Config)
 

@app.route('/')
def index():
    return render_template('index.html', lists=getLists(),cards=getCards())


@app.route('/',methods=['POST'])
def test():
    name=request.form.get("card_name")
    addCard(name,request.form['submit_button'])
    return redirect('/')


@app.route('/move/<card_id>/<list_id>',methods=['GET','POST'])
def move(card_id,list_id):
    moveCard(card_id,list_id)
    return redirect('/')


@app.route('/remove/<card_id>',methods=['GET','POST'])
def remove(card_id):
    removeCard(card_id)
    return redirect('/')

if __name__ == '__main__':
    app.run()
