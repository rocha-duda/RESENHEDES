import random


class HackathonSystem:

    def __init__(self, team):
        self.team = team

    def calcular_forca(self):

        total = 0

        for membro in self.team.membros:

            poder = (
                membro.programacao * 0.45 +
                membro.hardware * 0.25 +
                membro.aura * 0.10 +
                membro.sociabilidade * 0.10 +
                membro.energia * 0.10
            )

            # burnout reduz performance
            poder -= membro.burnout * 0.3

            # clutch ajuda MUITO
            if "clutch" in membro.traits:
                poder += 20

            # preguiçoso atrapalha
            if "preguicoso" in membro.traits:
                poder -= 10

            # perfeccionista
            if "perfeccionista" in membro.traits:
                poder += 8

            total += poder

        # química impacta
        quimica = self.team.calcular_quimica()

        total += quimica * 1.5

        return int(total)

    # =====================================================
    # EVENTOS DURANTE HACKATHON
    # =====================================================

    def evento_hackathon(self):

        membros = self.team.membros

        evento = random.choice([
            "bug",
            "briga",
            "genio",
            "colapso",
            "gambiarra",
            "professor"
        ])

        # =========================================

        if evento == "bug":

            pessoa = random.choice(membros)

            print("\n🐛 BUG CRÍTICO")
            print(f'{pessoa.nome}: "PAROU DE FUNCIONAR DO NADA."')

            pessoa.burnout += 10
            pessoa.energia -= 10

        # =========================================

        elif evento == "briga":

            a, b = random.sample(membros, 2)

            print("\n💥 BRIGA")

            falas = [
                f'{a.nome}: "Quem fez essa função horrorosa?"\n{b.nome}: "Funcionava na minha máquina."',

                f'{a.nome}: "Você sumiu a sprint inteira."\n{b.nome}: "Eu tava pensando na arquitetura."',

                f'{a.nome}: "O deploy morreu."\n{b.nome}: "Então revive."'
            ]

            print(random.choice(falas))

            a.relacoes[b.nome] -= 15
            b.relacoes[a.nome] -= 15

        # =========================================

        elif evento == "genio":

            pessoa = random.choice(membros)

            print("\n🧠 MOMENTO GÊNIO")

            print(f"{pessoa.nome} resolveu um bug impossível às 3 da manhã.")

            pessoa.programacao += 5
            pessoa.aura += 10

        # =========================================

        elif evento == "colapso":

            pessoa = random.choice(membros)

            print("\n💀 COLAPSO MENTAL")

            print(f'{pessoa.nome}: "EU NÃO AGUENTO MAIS ESSA VIDA."')

            pessoa.burnout += 20
            pessoa.energia -= 20

        # =========================================

        elif evento == "gambiarra":

            pessoa = random.choice(membros)

            print("\n🛠️ GAMBIARRA")

            print(f'{pessoa.nome}: "Se ninguém mexer no código, funciona."')

            pessoa.programacao += 3

        # =========================================

        elif evento == "professor":

            print("\n👨‍🏫 PROFESSOR APARECEU")

            print('"Vocês mudaram o escopo igual eu pedi?"')

            for membro in membros:

                membro.sanidade -= 10
                membro.burnout += 5

    # =====================================================
    # INICIAR HACKATHON
    # =====================================================

    def iniciar_hackathon(self):

        print("\n===================================")
        print("🏆 HACKATHON INICIADO")
        print("===================================")

        # vários acontecimentos
        quantidade_eventos = random.randint(3, 6)

        for _ in range(quantidade_eventos):

            self.evento_hackathon()

        # força final
        sua_forca = self.calcular_forca()

        rival = random.randint(200, 700)

        print("\n===================================")
        print("RESULTADO FINAL")
        print("===================================")

        print(f"⚔️ Sua equipe: {sua_forca}")
        print(f"👿 Rival: {rival}")

        # fator caos
        caos = random.randint(-80, 80)

        sua_forca += caos

        print(f"\n🎲 Caos da apresentação: {caos}")

        # resultado
        if sua_forca > rival:

            print("\n🏆 VITÓRIA ABSURDA")

            for membro in self.team.membros:

                membro.aura += 15
                membro.energia -= 10

        else:

            print("\n💀 DERROTA HUMILHANTE")

            for membro in self.team.membros:

                membro.burnout += 15
                membro.sociabilidade -= 5