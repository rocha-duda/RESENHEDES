import random


def evento_bug(team):
    """Um membro encontrou um bug crítico"""
    
    pessoa = random.choice(team.membros)

    print("\n🐛 BUG CRÍTICO")
    print(f'{pessoa.nome}: "O projeto parou de funcionar do nada."')

    pessoa.burnout += 10
    pessoa.energia -= 10
