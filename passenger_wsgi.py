from flask import Flask, import os, import sys, render_template

app = Flask(__name__)

@app.route("/")
def user():
    return 'Hello World'
    # return render_template("index1.html")

if __name__ == "__main__":
    app.run(debug=True)