import random


class Player:
    def __init__(self, nome):
        self.nome = nome

        # =========================
        # ATRIBUTOS
        # =========================

        self.programacao = random.randint(20, 100)
        self.hardware = random.randint(20, 100)
        self.aura = random.randint(20, 100)
        self.burnout = random.randint(0, 30)
        self.sociabilidade = random.randint(20, 100)
        self.energia = random.randint(50, 100)
        self.forca = random.randint(20, 100)

        # =========================
        # CARACTERÍSTICAS
        # =========================

        traits_com_peso = {
            "fofoqueiro": 10,
            "preguicoso": 10,
            "azarado": 10,
            "dramatico": 8,
            "competitivo": 8,
            "caotico": 7,
            "workaholic": 5,
            "manipulador": 4,
            "perfeccionista": 4,
            "clutch": 2,
            "maromba": 3,
            "falsidade": 1
        }

        # quantidade de traits
        quantidade_traits = random.choices(
            [0, 1, 2, 3],
            weights=[10, 35, 40, 15]
        )[0]

        self.traits = []

        lista_traits = list(traits_com_peso.keys())
        pesos = list(traits_com_peso.values())

        while len(self.traits) < quantidade_traits:
            trait = random.choices(lista_traits, weights=pesos)[0]

            if trait not in self.traits:
                self.traits.append(trait)

        # =========================
        # RELAÇÕES
        # =========================

        self.relacoes = {}

    def mostrar_status(self):
        print(f"\n==============================")
        print(f"{self.nome}")
        print(f"==============================")

        print(f"💻 Programação: {self.programacao}")
        print(f"🔌 Hardware: {self.hardware}")
        print(f"✨ Aura: {self.aura}")
        print(f"🔥 Burnout: {self.burnout}")
        print(f"🗣️ Sociabilidade: {self.sociabilidade}")
        print(f"⚡ Energia: {self.energia}")
        print(f"💪 Força: {self.forca}")

        if len(self.traits) > 0:
            print(f"🎭 Traits: {', '.join(self.traits)}")
        else:
            print("🎭 Traits: Nenhuma")