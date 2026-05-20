import random


def evento_colapso_mental(team):
    """Um membro sofre colapso por excesso de burnout"""
    
    pessoa = random.choice(team.membros)

    print("\n💀 COLAPSO")
    print(f'{pessoa.nome}: "EU NÃO AGUENTO MAIS."')

    pessoa.sociabilidade -= 10
    pessoa.energia -= 20
    pessoa.burnout += 15
