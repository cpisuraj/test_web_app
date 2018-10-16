'''
Created on Oct 16, 2018

@author: cpisuraj
'''
from flask import Flask, flash, redirect, render_template, request, session, abort
#from flask import Flask
#from flask.templating import render_template
app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
    
    