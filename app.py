import re
import time

from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from imgur_data import test_test

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ""

db = SQLAlchemy(app)


class ImageSearch(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String, nullable=False)
    when = db.Column(db.DateTime, server_default=db.func.now())
    
    def __init__(self, term):
        self.term = term
    
    
# A simple home route that renders index.html
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/imagesearch/<path:search_query>")
def img_search(search_query):
    
    ## Save the "term" and "when"
    term = search_query
    when = int(time.time())
    
    ## call a func thar returns (imgur data?)
    ## {"url":"","snippet":"","thumbnail":"","context":"" }
    
    test = test_test(12)
    return term + " " + str(test)


# Show search history with 'offset' amount of queries (default = 10).    
@app.route("/api/latest/imagesearch")
def history(offset=10):
    
    offset = request.args.get("offset", offset)
    
    ###Database search for history with offset queries
    
    
    return str(offset)
    

# Runs server.
if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 8080)