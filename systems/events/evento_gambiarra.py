import random


def evento_gambiarra(team):
    """Um membro faz uma gambiarra criativa"""
    
    pessoa = random.choice(team.membros)

    print("\n🛠️ GAMBIARRA")
    print(f'{pessoa.nome}: "Se ninguém tocar no código, funciona."')

    pessoa.programacao += 3
    pessoa.aura += 5
