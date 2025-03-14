import flask

import json

from flask import (render_template,request)

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/invio_ricezione_http', methods=['POST'])
def invio_ricezione_http():
    titolo = request.form['titolo']
    anno = request.form['anno']
    scrittore = request.form['scrittore']
    genere = request.form['genere']
    casa_editrice = request.form['casa_editrice']
    with open('data.json', 'w') as file:
        data = {
                "title": titolo,
                "year": anno,
                "author": scrittore,
                "genre": genere,
                "publisher": casa_editrice
            }
        json.dump(data, file)
    return data

if __name__ == "__main__":
    app.run(debug=True, port=50001)