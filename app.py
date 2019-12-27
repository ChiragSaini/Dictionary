from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import json
from difflib import get_close_matches
import os

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w][:2]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = ("Did you mean '%s' instead beacuse i didn't get that word" % get_close_matches(w, data.keys())[0])
        return yn
    

app = Flask(__name__)
app.config["SECRET_KEY"] = "ShitThisIsAwesome"

class Infoform(FlaskForm):
    word = StringField("Type you word here:")
    submit = SubmitField("Submit it pup")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dictionary", methods=["GET", "POST"])
def infoform():
    word = "Life"
    form = Infoform()
    if form.validate_on_submit():
        word = form.word.data
        form.word.data = ""

    result = translate(word)
    return render_template("infoform2.html", form=form, word=word, result = result)


if __name__ == "__main__":
    app.run(debug=True)