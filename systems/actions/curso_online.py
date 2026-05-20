import random


def curso_online(team):
    """O time comprou um curso online (suspeito)"""
    
    print("\n📚 O time comprou um curso online suspeito.")

    chance = random.randint(1, 100)

    if chance <= 35:

        print("\n💀 ERA GOLPE.")

        for membro in team.membros:

            membro.aura -= 3

            membro.burnout += 5

    else:

        print("\n🔥 O curso era absurdo.")

        for membro in team.membros:

            ganho = random.randint(3, 12)

            membro.programacao += ganho

            print(f"{membro.nome} ganhou +{ganho} programação.")
