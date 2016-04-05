import re

from flask import Flask, render_template, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ""

db = SQLAlchemy(app)


class ImageSearch(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String, nullable = False)
    
    def __init__(self, url):
        self.url = url
    
    
# A simple home route that renders index.html
@app.route("/")
def index():
    return render_template("index.html")
    

# Runs server.
if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 8080)