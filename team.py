class Team:

    def __init__(self, nome):
        self.nome = nome
        self.membros = []

    def adicionar_membro(self, player):

        if player not in self.membros:
            self.membros.append(player)

    def mostrar_time(self):

        print(f"\n==============================")
        print(f"EQUIPE: {self.nome}")
        print(f"==============================")

        for membro in self.membros:
            print(f"- {membro.nome}")

    def calcular_quimica(self):

        total = 0
        quantidade = 0

        for player in self.membros:
            for outro in self.membros:

                if player != outro:

                    total += player.relacoes[outro.nome]
                    quantidade += 1

        if quantidade == 0:
            return 0

        return int(total / quantidade)

    def calcular_forca(self):

        total = 0

        for player in self.membros:

            forca_individual = (
                player.programacao * 0.35 +
                player.hardware * 0.25 +
                player.aura * 0.15 +
                player.sociabilidade * 0.10 +
                player.energia * 0.10 +
                player.forca * 0.05
            )

            # burnout reduz performance
            forca_individual -= player.burnout * 0.4

            # clutch ajuda MUITO
            if "clutch" in player.traits:
                forca_individual += 15

            # preguiçoso atrapalha
            if "preguicoso" in player.traits:
                forca_individual -= 10

            total += forca_individual

        # química afeta força final
        quimica = self.calcular_quimica()

        total += quimica * 2

        return int(total)

    def clima_do_time(self):

        quimica = self.calcular_quimica()

        if quimica >= 70:
            return "🔥 IRMANDADE ABSURDA"

        elif quimica >= 40:
            return "😎 Time unido"

        elif quimica >= 10:
            return "🙂 Time funcional"

        elif quimica >= -20:
            return "😬 Clima estranho"

        elif quimica >= -50:
            return "💀 Ambiente tóxico"

        else:
            return "☠️ ÓDIO COMPLETO"