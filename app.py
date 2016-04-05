import re

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ""

db = SQLAlchemy(app)


class ImageSearch(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    term = db.Column(db.String, nullable = False)
    when = db.Column(db.Integer, nullable = False)
    
    def __init__(self, url):
        self.temr = term
        self.when = when
    
    
# A simple home route that renders index.html
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/imagesearch/<path:search_query>")
def img_search(search_query):
    pass
    
@app.route("/api/latest/imagesearch")
def history():
    pass
    

# Runs server.
if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 8080)