import flask
import json
from flask import render_template, request, redirect, url_for

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
    return redirect(url_for('visualizza_dati'))

@app.route('/visualizza_dati')
def visualizza_dati():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return render_template('visualizza_dati.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, port=50001)