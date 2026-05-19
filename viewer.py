from flask import Flask, render_template
from database import players

app = Flask(__name__)


@app.route("/")
def home():

    return render_template(
        "index.html",
        players=players
    )


@app.route("/player/<path:nome>")
def ver_player(nome):

    player = next(
        (p for p in players if p.nome == nome),
        None
    )

    return render_template(
        "player.html",
        player=player
    )


@app.route("/relacoes/<path:nome>")
def ver_relacoes(nome):

    player = next(
        (p for p in players if p.nome == nome),
        None
    )

    return render_template(
        "relacoes.html",
        player=player
    )


app.run(debug=True)