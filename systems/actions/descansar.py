import random


def descansar(team):
    """O time descansou e recuperou energia"""
    
    print("\n😴 O time descansou.")

    for membro in team.membros:

        membro.energia += random.randint(10, 25)

        membro.burnout -= random.randint(5, 15)
