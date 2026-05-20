import random


def evento_academia(team):
    """Um membro maromba posta foto na academia"""
    
    pessoa = random.choice(team.membros)

    print("\n🏋️ ACADEMIA")
    print(f'{pessoa.nome} postou foto no espelho da academia.')

    pessoa.aura += 10
    pessoa.forca += 5
