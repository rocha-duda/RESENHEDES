from player import Player
import random

nomes = [
    "Adrian Widmer", "Alexandre Pinto de Souza Ferreira", "Andrei Boulhosa de Sant'anna",
    "Arthur Ribeiro de Cerqueira", "Breno de Moura Batista", "Caio Schneider Loureiro da Costa",
    "Charles Moese Lopes de Souza Filho", "Davih de Andrade Machado Borges Santos",
    "Diogo Rossi Sampaio", "Emanuele Santos Diniz Penteado", "Felipe Emmanouil Martires Stamoglou",
    "Felipe Spinola Farias", "Flávio Fox Sandes Araújo Fernandes",
    "Gabriel Campos Santos Pereira", "Gabriel Moreira Barbosa Aragão",
    "Gabriel Trindade Santana", "Giulia de Jesus Franca", "Gustavo Oliveira Ramos Cruz",
    "Iago Santana Alfaya", "Icaro Canela Teixeira de Almeida", "João Paulo Caldas Lucas",
    "João Vitor Fraga de Carvalho Santos", "Jose Auto Araujo Neto",
    "Júlia Batista Iervese", "Otávio Augusto Coelho Katibe", "Kauã Costa Gouveia",
    "Leonardo Andrade Gomes Alves", "Levi dos Santos Abreu",
    "Lucas Breda Lima Mascarenhas", "Lucca Torres Badaró Silvani",
    "Maria Eduarda Benfica Gonçalves", "Maria Eduarda Cunha Rocha",
    "Nicolas Almeida Lago", "Nicollas Matsuo Mendes dos Santos",
    "Pedro Boaventura Ferraz de Oliveira", "Pedro Quadros de Freitas",
    "Rodrigo Oliveira Peixoto", "Tiago Costa Gomes Vianna",
    "Victor Mendes Ferreira Bittencourt", "Vitor Lucena Fabianski Campos",
    "Yasmin da Silva Bonfim"
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