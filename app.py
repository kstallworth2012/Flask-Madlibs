from flask import Flask, render_template,request
from stories import story 

app = Flask(__name__)

@app.route("/")
def madlibs_home():
    return render_template("madlibs_form.html", title="Madlibs")

@app.route("/story")
def show_story():
    """Show the madlibs story"""
    words = story.generate(request.args)
    return render_template("story.html",words=words)