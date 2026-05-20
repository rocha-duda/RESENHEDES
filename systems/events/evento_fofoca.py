import random


def evento_fofoca(team):
    """Um fofoqueiro espalha boato sobre outro membro"""
    
    a, b = random.sample(team.membros, 2)

    print("\n🗣️ FOFOCA")
    print(f'{a.nome} espalhou que {b.nome} usa ChatGPT escondido.')

    b.relacoes[a.nome] -= 15
