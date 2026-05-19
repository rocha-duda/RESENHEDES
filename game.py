import random


class Game:

    def __init__(self, team):

        self.team = team

        self.dia = 1

        self.dinheiro = 500

        self.game_over = False

    def mostrar_status(self):

        print("\n===================================")
        print(f"📅 DIA {self.dia}")
        print("===================================")

        print(f"💰 Dinheiro: {self.dinheiro}")

        print(f"🧪 Química: {self.team.calcular_quimica()}")

        print(f"⚔️ Força: {self.team.calcular_forca()}")

        print(f"🌡️ Clima: {self.team.clima_do_time()}")

    def menu_acoes(self):

        print("\n==============================")
        print("AÇÕES")
        print("==============================")

        print("1 - Estudar programação")
        print("2 - Ir pra academia")
        print("3 - Descansar")
        print("4 - Fazer resenha")
        print("5 - Comprar curso online")
        print("6 - Participar de hackathon")
        print("0 - Sair")

    def executar_acao(self, escolha):

        # =========================
        # ESTUDAR
        # =========================

        if escolha == "1":

            print("\n💻 O time estudou programação.")

            for membro in self.team.membros:

                ganho = random.randint(1, 6)

                membro.programacao += ganho

                membro.energia -= random.randint(5, 15)

                membro.burnout += random.randint(3, 10)

        # =========================
        # ACADEMIA
        # =========================

        elif escolha == "2":

            print("\n🏋️ O time foi treinar.")

            for membro in self.team.membros:

                membro.forca += random.randint(1, 5)

                membro.aura += random.randint(1, 4)

                membro.energia -= random.randint(5, 10)

                # maromba ganha bônus
                if "maromba" in membro.traits:

                    membro.aura += 5

                    membro.forca += 5

        # =========================
        # DESCANSAR
        # =========================

        elif escolha == "3":

            print("\n😴 O time descansou.")

            for membro in self.team.membros:

                membro.energia += random.randint(10, 25)

                membro.burnout -= random.randint(5, 15)

        # =========================
        # RESENHA
        # =========================

        elif escolha == "4":

            print("\n🍻 O time saiu pra resenha.")

            for membro in self.team.membros:

                membro.sociabilidade += random.randint(1, 5)

            # aumenta relações
            for player in self.team.membros:
                for outro in self.team.membros:

                    if player != outro:

                        player.relacoes[outro.nome] += random.randint(1, 8)

        # =========================
        # CURSO ONLINE
        # =========================

        elif escolha == "5":

            custo = 100

            if self.dinheiro >= custo:

                self.dinheiro -= custo

                print("\n📚 Compraram um curso online suspeito.")

                sucesso = random.randint(1, 100)

                # golpe
                if sucesso <= 30:

                    print("\n💀 Era golpe.")

                    for membro in self.team.membros:

                        membro.sanidade -= 10

                else:

                    print("\n🔥 O curso era absurdo.")

                    for membro in self.team.membros:

                        membro.programacao += random.randint(3, 10)

            else:

                print("\n💸 Sem dinheiro.")

        # =========================
        # HACKATHON
        # =========================

        elif escolha == "6":

            print("\n🏆 Participando de hackathon...")

            forca = self.team.calcular_forca()

            rival = random.randint(150, 600)

            print(f"\n⚔️ Sua força: {forca}")
            print(f"👿 Rival: {rival}")

            if forca > rival:

                premio = random.randint(100, 400)

                print(f"\n🏆 Vitória. +{premio}$")

                self.dinheiro += premio

            else:

                print("\n💀 Derrota humilhante.")

                for membro in self.team.membros:

                    membro.burnout += 10

                    membro.energia -= 15

        elif escolha == "0":

            self.game_over = True

    def atualizar_estado(self):

        for membro in self.team.membros:

            membro.energia = max(0, min(100, membro.energia))

            membro.burnout = max(0, min(100, membro.burnout))

            membro.programacao = max(0, min(100, membro.programacao))

            membro.forca = max(0, min(100, membro.forca))

            membro.aura = max(0, min(100, membro.aura))

        # derrota financeira
        if self.dinheiro <= -200:

            print("\n💀 O time faliu.")

            self.game_over = True

        self.dia += 1