from database import players
from team_select import escolher_time
from resenha import fazer_resenha

# Importar os sistemas de forma modular
from systems.events import gerar_evento
from systems.actions import estudar_programacao, ir_academia, descansar, curso_online
from systems.hackathon import iniciar_hackathon

time_player = escolher_time(players)


while True:

    print("""
========================

1 Evento
2 Ver time
3 Estudar
4 Resenha
5 Academia
6 Descansar
7 Curso Online
8 Hackathon
0 Sair

========================
""")

    escolha = input("> ")

    if escolha == "1":
        gerar_evento(time_player)

    elif escolha == "2":
        time_player.mostrar_time()

    elif escolha == "3":
        estudar_programacao(time_player)

    elif escolha == "4":
        fazer_resenha(time_player)

    elif escolha == "5":
        ir_academia(time_player)

    elif escolha == "6":
        descansar(time_player)

    elif escolha == "7":
        curso_online(time_player)

    elif escolha == "8":
        iniciar_hackathon(time_player)

    elif escolha == "0":
        break


print("\n===== FIM =====")

time_player.mostrar_time()

print(
    f"\n🧪 {time_player.calcular_quimica()}"
)

print(
    f"⚔️ {time_player.calcular_forca()}"
)