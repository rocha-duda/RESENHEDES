import random


def ir_academia(team):
    """O time foi treinar na academia"""
    
    print("\n🏋️ O time foi treinar.")

    for membro in team.membros:

        membro.forca += random.randint(2, 7)

        membro.aura += random.randint(1, 5)

        membro.energia -= random.randint(5, 15)

        if "maromba" in membro.traits:

            membro.forca += 5
            membro.aura += 5

            print(f"{membro.nome} ativou o buff MAROMBA.")
