from player import Player
import random

nomes = [
    "Adriano Widperador", "Alixandre Pinto", "Andrey Sacana",
    "Arthur Cerca", "Breno de Moura", "Caio Schneider",
    "Charles Moese", "Davihhhhh",
    "Diogo Rossi", "Emanuele Santos", "Felipe Stamina",
    "Felipe Fatz Farias", "F. Raposo",
    "Gabriel Fields", "Gabriel Aragão",
    "Gabriel Santíssima Trindade", "G. Jesus", "Gustavo Cruz",
    "Iago Alface", "Icaro Cravo e Canela", "João Paulo Caldas",
    "João Fragrâncias", "Jose Baixo",
    "Júlia Reverso", "Otávio Katibe", "Kauã Frente",
    "Leonardo Andrade", "Levi Abril",
    "Lucas Breda", "Lucca Nine Eleven",
    "Maria Porto", "Maria Eduarda Rocha",
    "Nicolas Rio", "Nicollas Matsuo",
    "Pedro Oliveira", "Pedro Pinturas",
    "Rodrigo Pedala Peixoto", "Tiago Frente",
    "Victor Memes", "Vitor Lucena",
    "Yasmin Bonfim"
]

players = []

for nome in nomes:
    players.append(Player(nome))


def gerar_relacoes():

    for player in players:

        for outro in players:

            if player == outro:
                continue

            relacao = random.randint(-50, 100)

            if player.sociabilidade > 70:
                relacao += 10

            if "falsidade" in player.traits:
                relacao += random.randint(-30, 30)

            if "fofoqueiro" in player.traits:
                relacao += random.randint(-15, 10)

            relacao = max(-100, min(100, relacao))

            player.relacoes[outro.nome] = relacao


gerar_relacoes()