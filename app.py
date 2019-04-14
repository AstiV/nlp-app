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

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        # NLP
        blob = TextBlob(rawtext)
        received_text = blob
        sentiment = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        number_of_tokens = len(list(blob.words))

    return render_template('index.html', received_text = received_text, sentiment = sentiment, subjectivity = subjectivity, number_of_tokens = number_of_tokens)

#TODO change this for production! (debug=True only for dev mode)
if __name__ == '__main__':
    app.run(debug=True)

