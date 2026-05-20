import random
import time

def fazer_resenha(team):
    membros = team.membros

    if len(membros) < 3:
        print("\nSem gente suficiente pra resenha.")
        return

    grupo = random.sample(
        membros,
        min(random.randint(3, 5), len(membros))
    )

    print("\n🍻 RESENHA DA EQUIPE")
    print("=" * 40)
    time.sleep(0.8)

    conversas = [
        [
            "{a}: Mano, e se a gente só entregar um powerpoint?",
            "{b}: Sem sistema?",
            "{a}: MVP.",
            "{c}: Isso nem significa isso."
        ],
        [
            "{a}: Eu tenho uma ideia revolucionária.",
            "{b}: Lá vem.",
            "{a}: Usar IA pra fazer tudo.",
            "{c}: Essa era literalmente nossa estratégia."
        ],
        [
            "{a}: Quem apagou produção?",
            "{b}: Produção tinha backup?",
            "{c}: PRODUÇÃO TINHA O QUÊ???"
        ],
        [
            "{a}: Se ganhar hackathon eu tatuo o nome do grupo.",
            "{b}: Printado.",
            "{c}: Eu sou testemunha."
        ],
        [
            "{a}: Bora abrir startup.",
            "{b}: Nem projeto da matéria terminou.",
            "{c}: Pensamento de CEO."
        ],
        [
            "{a}: Eu vi um curso que promete virar sênior em 8 horas.",
            "{b}: Comprou?",
            "{a}: Comprei dois."
        ],
        [
            "{a}: Vocês perceberam que ninguém entende nosso código?",
            "{b}: Segurança por obscuridade.",
            "{c}: Visionários."
        ],
        [
            "{a}: Se tirar nota baixa a culpa é do hardware.",
            "{b}: Mas nem tem hardware.",
            "{c}: Exatamente."
        ],
        [
            "{a}: Alguém testou antes de subir?",
            "{b}: Testar é duvidar da própria capacidade.",
            "{c}: Vou atualizar meu currículo."
        ],
        [
            "{a}: HTML é linguagem de programação?",
            "{b}: Sai da minha frente.",
            "{c}: Ele só fez uma pergunta..."
        ],
        [
            "{a}: Fiz um script pra automatizar aquela tarefa.",
            "{b}: Levou quanto tempo?",
            "{a}: Três dias pra automatizar algo de cinco minutos."
        ],
        [
            "{a}: O projeto roda perfeitamente na minha máquina.",
            "{b}: Beleza, vamos entregar sua máquina pro cliente.",
            "{c}: Solução de arquitetura invejável."
        ],
        [
            "{a}: Descobri como fazer overclock no micro-ondas.",
            "{b}: Pra quê?",
            "{c}: Pra esquentar o miojo em 1 minuto, óbvio."
        ],
        [
            "{a}: Eu não preciso de documentação.",
            "{b}: O código é autoexplicativo?",
            "{a}: Não, eu só confio na minha intuição."
        ],
        [
            "{a}: Se a gente ignorar os warnings, eles somem.",
            "{b}: O compilador tá literalmente chorando.",
            "{c}: Choro é livre, o deploy também."
        ]
    ]

    cena = random.choice(conversas)

    nomes = {
        "a": grupo[0].nome,
        "b": grupo[1].nome,
        "c": grupo[2].nome
    }

    for fala in cena:
        print(fala.format(**nomes))
        time.sleep(0.6)

    print()
    time.sleep(1.0)

    evento = random.choices(
        [
            "mitada",
            "brainrot",
            "fofoca",
            "conexao",
            "climao",
            "descanso",
            "gambiarra",
            "maromba",
            "treta_tech"
        ],
        weights=[15, 10, 10, 15, 10, 15, 10, 5, 10]
    )[0]

    if evento == "mitada":
        pessoa = random.choice(grupo)
        print(f"🔥 {pessoa.nome} contou uma história absurda e virou lenda.")
        print(f"  ✅ {pessoa.nome}: +12 Aura, +5 Sociabilidade")
        pessoa.aura += 12
        pessoa.sociabilidade += 5
        for p in grupo:
            p.burnout = max(0, p.burnout - 4)
        print(f"  ⬇️ Todos: -4 Burnout")
        time.sleep(1.0)

    elif evento == "brainrot":
        print("🧠 A conversa entrou em reels, teoria maluca e vídeos inúteis.")
        time.sleep(0.5)
        for p in grupo:
            perda = random.randint(1, 6)
            p.programacao = max(0, p.programacao - perda)
            p.burnout = max(0, p.burnout - 8)
            print(f"  {p.nome}: -{perda} Programação, -8 Burnout")
            time.sleep(0.3)
        print("✓ Todos perderam inteligência mas descansaram.")
        time.sleep(1.0)

    elif evento == "fofoca":
        a, b = random.sample(grupo, 2)
        print(f"👀 {a.nome} espalhou um boato sobre {b.nome}.")
        time.sleep(0.5)
        if hasattr(a, 'traits') and "fofoqueiro" in a.traits:
            print("FOFOQUEIRO PROFISSIONAL → ninguém descobriu.")
            a.aura += 5
            print(f"  ✅ {a.nome}: +5 Aura")
        else:
            print("Pegaram na mentira.")
            a.aura -= 10
            print(f"  ❌ {a.nome}: -10 Aura")
        b.sociabilidade -= 5
        print(f"  ❌ {b.nome}: -5 Sociabilidade")
        time.sleep(1.0)

    elif evento == "conexao":
        print("🤝 O grupo entrou numa conversa profunda inesperada.")
        time.sleep(0.5)
        for p in grupo:
            ganho_relacao = 0
            p.sociabilidade += 6
            p.burnout = max(0, p.burnout - 10)
            for outro in grupo:
                if p != outro:
                    atual = p.relacoes.get(outro.nome, 0)
                    ganho = random.randint(5, 15)
                    ganho_relacao += ganho
                    p.relacoes[outro.nome] = min(100, atual + ganho)
            print(f"  ✅ {p.nome}: +6 Sociabilidade, -10 Burnout, +{ganho_relacao} Relação")
            time.sleep(0.3)

    elif evento == "climao":
        a, b = random.sample(grupo, 2)
        print(f"💀 {a.nome} fez um comentário extremamente cringe.")
        time.sleep(0.5)
        a.aura -= 12
        b.aura += 5
        atual = a.relacoes.get(b.nome, 0)
        a.relacoes[b.nome] = atual - 20
        print(f"  ❌ {a.nome}: -12 Aura, -20 Relação com {b.nome}")
        print(f"  ✅ {b.nome}: +5 Aura")
        time.sleep(1.0)

    elif evento == "gambiarra":
        pessoa = random.choice(grupo)
        print(f"🔧 {pessoa.nome} ensinou um atalho bizarro de código e montagem.")
        time.sleep(0.5)
        pessoa.programacao += 5
        pessoa.hardware += 5
        pessoa.aura -= 8
        print(f"  ✅ {pessoa.nome}: +5 Programação, +5 Hardware")
        print(f"  ❌ {pessoa.nome}: -8 Aura")
        time.sleep(0.3)
        for p in grupo:
            if p != pessoa:
                p.burnout += 3
                print(f"  ❌ {p.nome}: +3 Burnout (by {pessoa.nome})")
                time.sleep(0.2)

    elif evento == "maromba":
        print("💪 A resenha virou sobre academia, whey e postura na cadeira.")
        time.sleep(0.5)
        for p in grupo:
            p.forca += 5
            p.energia = max(0, p.energia - 5)
            p.sociabilidade += 2
            print(f"  {p.nome}: +5 Força, -5 Energia, +2 Sociabilidade")
            time.sleep(0.3)

    elif evento == "treta_tech":
        a, b = random.sample(grupo, 2)
        print(f"⚔️ {a.nome} e {b.nome} começaram a brigar por causa de framework e SO.")
        time.sleep(0.5)
        a.programacao += 3
        b.hardware += 3
        a.burnout += 10
        b.burnout += 10
        print(f"  ✅ {a.nome}: +3 Programação")
        print(f"  ❌ {a.nome}: +10 Burnout")
        print(f"  ✅ {b.nome}: +3 Hardware")
        print(f"  ❌ {b.nome}: +10 Burnout")
        time.sleep(0.3)
        for p in grupo:
            if p not in (a, b):
                p.aura -= 2
                print(f"  ❌ {p.nome}: -2 Aura")
                time.sleep(0.2)

    else:
        print("😴 Foi só uma resenha saudável.")
        time.sleep(0.5)
        for p in grupo:
            p.energia += 8
            p.burnout = max(0, p.burnout - 12)
            print(f"  ✅ {p.nome}: +8 Energia, -12 Burnout")
            time.sleep(0.3)

    print("=" * 40)