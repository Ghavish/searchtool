from flask import Flask, render_template,redirect,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/imagesearch')
def imagesearch():
    return render_template("imagesearch.html")

@app.route('/advancedsearch')
def advancedsearch():
    return render_template("advancedsearch.html")
