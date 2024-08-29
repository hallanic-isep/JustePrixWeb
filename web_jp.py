import random
from datetime import datetime

import flask
from flask import Flask

import juste_prix

app = Flask(__name__)


@app.route("/hello")
def index():
    return 'Hello from Flask!'

@app.route('/')
def toto():
    donnees_jeu["cible"] = random.randint(1,10)
    donnees_jeu["compteur"] = 1
    return flask.render_template(
        "index.html",
        heure_connexion = datetime.now()
    )

donnees_jeu = {}

@app.route('/jeu')
def jeu():
    donnees_jeu["compteur"] += 1
    return flask.render_template("jeu.html", i = donnees_jeu["compteur"])

@app.route('/verif')
def verif():
    essai = int(flask.request.values["essai"])
    if donnees_jeu["cible"] == essai:
        return flask.render_template(
            "verif.html",
            msg="BRAVO !!!",
            action="/",
            bouton="Nouvelle partie"
        )
    if donnees_jeu["cible"] < essai:
        return flask.render_template(
            "verif.html",
            msg="TROP ELEVE...",
            action="/jeu",
            bouton="Nouvel essai"
        )
    if donnees_jeu["cible"] > essai:
        return flask.render_template(
            "verif.html",
            msg="TROP PEU...",
            action="/jeu",
            bouton="Nouvel essai"
        )


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
