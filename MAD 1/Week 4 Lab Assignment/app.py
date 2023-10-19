import pandas as pd
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        value = request.form["id_value"]
        return render_template("tst.html", display_name = value)

if __name__ == '__main__':
    app.debug = True
    app.run()