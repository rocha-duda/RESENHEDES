import random


def evento_trairagem(team):
    """Um membro falso culpa outro de um bug"""
    
    a, b = random.sample(team.membros, 2)

    print("\n🐍 TRAIRAGEM")
    print(f'{a.nome} jogou a culpa do bug em {b.nome}.')

    b.relacoes[a.nome] -= 25
    a.relacoes[b.nome] -= 10
