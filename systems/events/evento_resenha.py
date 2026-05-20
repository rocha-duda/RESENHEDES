import random


def evento_resenha(team):
    """Dois membros saem pra resenha"""
    
    a, b = random.sample(team.membros, 2)

    falas = [
        f'{a.nome}: "Bora meter um podrão depois da aula?"',
        f'{b.nome}: "A gente não sabe nem se vai passar na matéria."',

        f'{a.nome}: "O código tá horrível."',
        f'{b.nome}: "Mas tá funcionando."'
    ]

    print("\n🍻 RESENHA")
    print(random.choice(falas))

    a.relacoes[b.nome] += 5
    b.relacoes[a.nome] += 5
