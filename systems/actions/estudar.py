import random


def estudar_programacao(team):
    """O time estudou programação"""
    
    print("\n💻 O time decidiu estudar programação.")

    for membro in team.membros:

        ganho = random.randint(2, 8)

        membro.programacao += ganho

        membro.energia -= random.randint(5, 12)

        membro.burnout += random.randint(2, 8)

        print(f"{membro.nome} ganhou +{ganho} programação.")
