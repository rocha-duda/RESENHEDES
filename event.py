import random


class EventSystem:

    def __init__(self, team):
        self.team = team

    def gerar_evento(self):

        membros = self.team.membros

        if len(membros) < 2:
            return

        evento_pool = []

        # =========================
        # EVENTOS BASE
        # =========================

        evento_pool.extend([
            self.evento_resenha,
            self.evento_bug,
            self.evento_gambiarra
        ])

        # =========================
        # EVENTOS CONTEXTUAIS
        # =========================

        for membro in membros:

            # burnout
            if membro.burnout >= 70:
                evento_pool.append(self.evento_colapso_mental)

            # fofoqueiro
            if "fofoqueiro" in membro.traits:
                evento_pool.append(self.evento_fofoca)

            # falsidade
            if "falsidade" in membro.traits:
                evento_pool.append(self.evento_trairagem)

            # maromba
            if "maromba" in membro.traits:
                evento_pool.append(self.evento_academia)

        evento = random.choice(evento_pool)

        evento()

    # =====================================================
    # EVENTOS
    # =====================================================

    def evento_resenha(self):

        a, b = random.sample(self.team.membros, 2)

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

    def evento_bug(self):

        pessoa = random.choice(self.team.membros)

        print("\n🐛 BUG CRÍTICO")
        print(f'{pessoa.nome}: "O projeto parou de funcionar do nada."')

        pessoa.burnout += 10
        pessoa.energia -= 10

    def evento_gambiarra(self):

        pessoa = random.choice(self.team.membros)

        print("\n🛠️ GAMBIARRA")
        print(f'{pessoa.nome}: "Se ninguém tocar no código, funciona."')

        pessoa.programacao += 3
        pessoa.aura += 5

    def evento_fofoca(self):

        a, b = random.sample(self.team.membros, 2)

        print("\n🗣️ FOFOCA")
        print(f'{a.nome} espalhou que {b.nome} usa ChatGPT escondido.')

        b.relacoes[a.nome] -= 15

    def evento_trairagem(self):

        a, b = random.sample(self.team.membros, 2)

        print("\n🐍 TRAIRAGEM")
        print(f'{a.nome} jogou a culpa do bug em {b.nome}.')

        b.relacoes[a.nome] -= 25
        a.relacoes[b.nome] -= 10

    def evento_colapso_mental(self):

        pessoa = random.choice(self.team.membros)

        print("\n💀 COLAPSO")
        print(f'{pessoa.nome}: "EU NÃO AGUENTO MAIS."')

        pessoa.sociabilidade -= 10
        pessoa.energia -= 20
        pessoa.burnout += 15

    def evento_academia(self):

        pessoa = random.choice(self.team.membros)

        print("\n🏋️ ACADEMIA")
        print(f'{pessoa.nome} postou foto no espelho da academia.')

        pessoa.aura += 10
        pessoa.forca += 5