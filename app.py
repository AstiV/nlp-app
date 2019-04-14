from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap

#NLP
from textblob import TextBlob, Word
import random

import time

# Configure application
app = Flask(__name__)
bootstrap = Bootstrap(app) 

# Routing
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    start = time.time()
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        # NLP: get text and calculate score
        blob = TextBlob(rawtext)
        received_text = blob
        sentiment = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        number_of_tokens = len(list(blob.words))

        # NLP: the funky stuff
        nouns = list()
        for word, tag in blob.tags:
            if tag == 'NN':
                nouns.append(word.lemmatize())
                len_of_words = len(nouns)
                rand_words = random.sample(nouns,len(nouns))
                final_word = list()
                for item in rand_words:
                    word = Word(item).pluralize()
                    final_word.append(word)
                    summary = final_word
                    end = time.time()
                    final_time = end-start



    return render_template('index.html', received_text = received_text, sentiment = sentiment, subjectivity = subjectivity, number_of_tokens = number_of_tokens, summary = summary, final_time = final_time)

#TODO change this for production! (debug=True only for dev mode)
if __name__ == '__main__':
    app.run(debug=True)

