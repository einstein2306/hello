from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello world</h1>"


@app.route("/hello")
def h1():
    return render_template("hello.html")
