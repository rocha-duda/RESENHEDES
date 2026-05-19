from database import players

from team_select import escolher_time

from event import EventSystem
from actions import ActionSystem
from hackathon import HackathonSystem


time_player = escolher_time(
    players
)

event_system = EventSystem(
    time_player
)

action_system = ActionSystem(
    time_player
)

hackathon_system = HackathonSystem(
    time_player
)


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
        event_system.gerar_evento()

    elif escolha == "2":
        time_player.mostrar_time()

    elif escolha == "3":
        action_system.estudar_programacao()

    elif escolha == "4":
        action_system.fazer_resenha()

    elif escolha == "5":
        action_system.ir_academia()

    elif escolha == "6":
        action_system.descansar()

    elif escolha == "7":
        action_system.curso_online()

    elif escolha == "8":
        hackathon_system.iniciar_hackathon()

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