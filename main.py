from player import Player
from team import Team
import random
from event import EventSystem
from actions import ActionSystem
from hackathon import HackathonSystem

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

# =========================
# CRIAR PLAYERS
# =========================

for nome in nomes:
    player = Player(nome)
    players.append(player)

# =========================
# GERAR RELAÇÕES
# =========================

for player in players:
    for outro in players:

        if player != outro:

            relacao = random.randint(-50, 100)

            # bônus sociável
            if player.sociabilidade > 70 and outro.sociabilidade > 70:
                relacao += 10

            # falsidade
            if "falsidade" in player.traits:
                relacao += random.randint(-30, 30)

            # fofoqueiro
            if "fofoqueiro" in player.traits:
                relacao += random.randint(-15, 10)

            relacao = max(-100, min(100, relacao))

            player.relacoes[outro.nome] = relacao

# =========================
# MOSTRAR STATUS
# =========================

for player in players:

    player.mostrar_status()

# =========================
# TESTE DE RELAÇÕES
# =========================

print("\n==============================")
print("RELACOES")
print("==============================")

player_aleatorio = random.choice(players)

print(f"\nRelações de {player_aleatorio.nome}:\n")

for nome, valor in player_aleatorio.relacoes.items():

    emoji = "😐"

    if valor >= 70:
        emoji = "🔥"

    elif valor >= 30:
        emoji = "🙂"

    elif valor <= -50:
        emoji = "💀"

    elif valor <= -20:
        emoji = "😡"

    print(f"{emoji} {nome}: {valor}")

# =========================
# ESCOLHER TIME
# =========================

print("\n==============================")
print("MONTE SUA EQUIPE")
print("==============================")

for i, player in enumerate(players):

    print(f"\n[{i}] {player.nome}")

    print(
        f"💻 Prog:{player.programacao} "
        f"🔌 Hard:{player.hardware} "
        f"✨ Aura:{player.aura} "
        f"🗣️ Social:{player.sociabilidade}"
    )

    if len(player.traits) > 0:
        print(f"🎭 {', '.join(player.traits)}")

    else:
        print("🎭 Nenhuma")

# =========================
# CRIAR TIME
# =========================

time_player = Team("Seu Time")

while len(time_player.membros) < 5:

    try:

        escolha = int(input("\nEscolha o número do integrante: "))

        escolhido = players[escolha]

        if escolhido not in time_player.membros:

            time_player.adicionar_membro(escolhido)

            print(f"\n✅ {escolhido.nome} entrou na equipe.")

        else:
            print("\n⚠️ Essa pessoa já está no time.")

    except:
        print("\n❌ Escolha inválida.")

event_system = EventSystem(time_player)
action_system = ActionSystem(time_player)
hackathon_system = HackathonSystem(time_player)
while True:

    print("\n========================")
    print("1 - Gerar evento")
    print("2 - Ver time")
    print("3 - Estudar programação")
    print("4 - Fazer resenha")
    print("5 - Ir pra academia")
    print("6 - Descansar")
    print("7 - Curso online suspeito")
    print("8 - Participar de hackathon")
    print("0 - Sair")
    print("========================")

    escolha = input("Escolha: ")

    # EVENTO
    if escolha == "1":

        event_system.gerar_evento()

    # VER TIME
    elif escolha == "2":

        time_player.mostrar_time()

        for membro in time_player.membros:
            membro.mostrar_status()

    # ESTUDAR
    elif escolha == "3":

        action_system.estudar_programacao()

    # RESENHA
    elif escolha == "4":

        action_system.fazer_resenha()

    # ACADEMIA
    elif escolha == "5":

        action_system.ir_academia()

    # DESCANSAR
    elif escolha == "6":

        action_system.descansar()

    # CURSO
    elif escolha == "7":

        action_system.curso_online()
    
    elif escolha == "8":

        hackathon_system.iniciar_hackathon()

    elif escolha == "0":

        break

# =========================
# MOSTRAR TIME
# =========================

time_player.mostrar_time()

print(f"\n🧪 Química: {time_player.calcular_quimica()}")
print(f"⚔️ Força Total: {time_player.calcular_forca()}")
print(f"🌡️ Clima: {time_player.clima_do_time()}")