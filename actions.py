import random


class ActionSystem:

    def __init__(self, team):
        team = team

    # =====================================================
    # ESTUDAR
    # =====================================================

    def estudar_programacao(self):

        print("\n💻 O time decidiu estudar programação.")

        for membro in team.membros:

            ganho = random.randint(2, 8)

            membro.programacao += ganho

            membro.energia -= random.randint(5, 12)

            membro.burnout += random.randint(2, 8)

            print(f"{membro.nome} ganhou +{ganho} programação.")

    # =====================================================
    # RESENHA
    # =====================================================

    # def fazer_resenha(self):

    #     print("\n🍻 O time saiu pra resenha.")

    #     for membro in team.membros:

    #         membro.sociabilidade += random.randint(1, 5)

    #     for a in team.membros:
    #         for b in team.membros:

    #             if a != b:

    #                 aumento = random.randint(1, 10)

    #                 a.relacoes[b.nome] += aumento

    # =====================================================
    # ACADEMIA
    # =====================================================

    def ir_academia(self):

        print("\n🏋️ O time foi treinar.")

        for membro in team.membros:

            membro.forca += random.randint(2, 7)

            membro.aura += random.randint(1, 5)

            membro.energia -= random.randint(5, 15)

            if "maromba" in membro.traits:

                membro.forca += 5
                membro.aura += 5

                print(f"{membro.nome} ativou o buff MAROMBA.")

    # =====================================================
    # DESCANSAR
    # =====================================================

    def descansar(self):

        print("\n😴 O time descansou.")

        for membro in team.membros:

            membro.energia += random.randint(10, 25)

            membro.burnout -= random.randint(5, 15)

    # =====================================================
    # CURSO ONLINE
    # =====================================================

    def curso_online(self):

        print("\n📚 O time comprou um curso online suspeito.")

        chance = random.randint(1, 100)

        # golpe
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