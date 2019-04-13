from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap

#NLP
from textblob import TextBlob, Word
import random

# Configure application
app = Flask(__name__)
bootstrap = Bootstrap(app) 

# Routing
@app.route('/')
def index():
    return render_template('index.html')

#TODO change this for production! (debug=True only for dev mode)
if __name__ == '__main__':
    app.run(debug=True)

