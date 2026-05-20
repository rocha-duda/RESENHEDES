import random
import string
import time


def gerar_equipe_rival():
    """Gera uma equipe rival com nomes aleatórios"""
    
    sobrenomes = [
        "Silva", "Santos", "Oliveira", "Souza", "Costa", "Martins",
        "Ferreira", "Alves", "Gomes", "Pereira", "Carvalho", "Barbosa"
    ]
    
    nomes = [
        "Lucas", "Felipe", "Bruno", "Diego", "Rafael", "João", "Pedro",
        "André", "Gustavo", "Carlos", "Leonardo", "Paulo", "Amanda",
        "Carolina", "Beatriz", "Jessica", "Marina", "Isabela"
    ]
    
    nomes_equipe = []
    for _ in range(3):
        nome = random.choice(nomes) + " " + random.choice(sobrenomes)
        nomes_equipe.append(nome)
    
    return nomes_equipe


def calcular_forca(team):
    """Calcula a força total do time para uma hackathon"""
    
    total = 0

    for membro in team.membros:

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
    quimica = team.calcular_quimica()
    total += quimica * 1.5

    return int(total)


def _evento_rodada_bug_nosso(team, pontos):
    """Evento: bug crítico no nosso código"""
    pessoa = random.choice(team.membros)
    print(f"\n🐛 BUG CRÍTICO NO CÓDIGO!")
    print(f"   {pessoa.nome}: 'PAROU DE FUNCIONAR DO NADA.'")
    time.sleep(0.5)
    pessoa.burnout += 10
    pessoa.energia -= 10
    pontos['seu_time'] -= 20
    print(f"   ⚠️ -20 pontos para seu time")
    time.sleep(1.0)
    return pontos


def _evento_rodada_bug_rival(pontos):
    """Evento: bug crítico no código rival"""
    print(f"\n🐛 BUG CRÍTICO NO RIVAL!")
    print(f"   O código rival parou de funcionar.")
    time.sleep(0.5)
    pontos['rival'] -= 25
    print(f"   ✅ +15 pontos para seu time")
    pontos['seu_time'] += 15
    time.sleep(1.0)
    return pontos


def _evento_rodada_genio(team, pontos):
    """Evento: momento de gênio"""
    pessoa = random.choice(team.membros)
    print(f"\n🧠 MOMENTO GÊNIO!")
    print(f"   {pessoa.nome} resolveu um bug impossível às 3 da manhã.")
    time.sleep(0.5)
    pessoa.programacao += 5
    pessoa.aura += 10
    pontos['seu_time'] += 30
    print(f"   ✅ +30 pontos para seu time")
    time.sleep(1.0)
    return pontos


def _evento_rodada_gambiarra(team, pontos):
    """Evento: gambiarra criativa"""
    pessoa = random.choice(team.membros)
    print(f"\n🛠️ GAMBIARRA!")
    print(f"   {pessoa.nome}: 'Se ninguém mexer no código, funciona.'")
    time.sleep(0.5)
    pessoa.programacao += 3
    pontos['seu_time'] += 15
    print(f"   ✅ +15 pontos para seu time")
    time.sleep(1.0)
    return pontos


def _evento_rodada_briga_interna(team, pontos):
    """Evento: briga entre membros do nosso time"""
    a, b = random.sample(team.membros, 2)
    print(f"\n💥 BRIGA INTERNA!")
    falas = [
        f'{a.nome}: "Quem fez essa função horrorosa?"\n{b.nome}: "Funcionava na minha máquina."',
        f'{a.nome}: "Você sumiu a sprint inteira."\n{b.nome}: "Eu tava pensando na arquitetura."',
        f'{a.nome}: "O deploy morreu."\n{b.nome}: "Então revive."'
    ]
    print(f"   {random.choice(falas)}")
    time.sleep(0.5)
    a.relacoes[b.nome] -= 15
    b.relacoes[a.nome] -= 15
    pontos['seu_time'] -= 15
    print(f"   ❌ -15 pontos para seu time (desorganização)")
    time.sleep(1.0)
    return pontos


def _evento_rodada_confronto_rival(team, pontos):
    """Evento: confronto direto com o rival"""
    print(f"\n⚔️ CONFRONTO DIRETO COM O RIVAL!")
    membro_seu = random.choice(team.membros)
    print(f"   {membro_seu.nome} e um rival começam a discutir tecnologia.")
    time.sleep(0.8)
    
    # Quem vence?
    if random.random() < 0.6:  # 60% de chance de ganhar
        print(f"   {membro_seu.nome} DESTROÇA o rival com argumentos.")
        membro_seu.aura += 8
        pontos['seu_time'] += 25
        pontos['rival'] -= 10
        print(f"   ✅ +25 pontos para seu time, -10 do rival")
    else:
        print(f"   {membro_seu.nome} leva uma derrota argumentativa.")
        membro_seu.aura -= 5
        pontos['seu_time'] -= 10
        print(f"   ❌ -10 pontos para seu time")
    
    time.sleep(1.0)
    return pontos


def _evento_rodada_caos(pontos):
    """Evento: caos aleatório"""
    print(f"\n🎲 CAOS PURO!")
    caos_events = [
        ("O WiFi cai da HACKATHON INTEIRA", -5, -5),
        ("A apresentação mudou de horário pra AGORA", -10, -10),
        ("Alguém derramou café na SALA DE CÓDIGO", -15, 0),
        ("Um dos jurados foi EMBORA", -20, 10),
    ]
    
    evento, seu_impacto, rival_impacto = random.choice(caos_events)
    print(f"   {evento}")
    time.sleep(0.5)
    
    pontos['seu_time'] += seu_impacto
    pontos['rival'] += rival_impacto
    
    if seu_impacto < 0:
        print(f"   ❌ {seu_impacto} pontos para seu time")
    if rival_impacto < 0:
        print(f"   ✅ {-rival_impacto} pontos salvos do rival")
    
    time.sleep(1.0)
    return pontos


def _evento_rodada_maluquice(team, pontos):
    """Evento: maluquice total"""
    print(f"\n🤪 MALUQUICE!")
    pessoa = random.choice(team.membros)
    
    maluquices = [
        f"{pessoa.nome} fez um código em uma mão só enquanto tomava café com a outra.",
        f"{pessoa.nome} começou a programar CANTANDO.",
        f"{pessoa.nome} descobriu que pode programar dormindo (e funciona).",
        f"{pessoa.nome} inverteu toda a lógica e VIROU GÊNIO (ou virou louco?).",
    ]
    
    print(f"   {random.choice(maluquices)}")
    time.sleep(0.8)
    
    if random.random() < 0.5:
        pontos['seu_time'] += 35
        pessoa.aura += 15
        pessoa.burnout -= 10
        print(f"   ✅ +35 pontos para seu time (FUNCIONOU!)")
    else:
        pontos['seu_time'] -= 25
        pessoa.burnout += 15
        print(f"   ❌ -25 pontos para seu time (Não funcionou...)")
    
    time.sleep(1.0)
    return pontos


def _evento_rodada_sprint(team, rival_team, pontos):
    """Evento: sprint final - todos ganham pontos baseado em força"""
    print(f"\n⚡ SPRINT FINAL!")
    
    seu_poder = calcular_forca(team)
    rival_poder = random.randint(150, 400)
    
    print(f"   Seu time: {seu_poder} pontos")
    print(f"   Rival: {rival_poder} pontos")
    time.sleep(0.5)
    
    if seu_poder > rival_poder:
        ganho = seu_poder - rival_poder
        pontos['seu_time'] += ganho
        print(f"   ✅ +{ganho} pontos para seu time")
    else:
        perda = rival_poder - seu_poder
        pontos['rival'] += perda
        print(f"   ❌ Rival ganha +{perda} pontos")
    
    time.sleep(1.0)
    return pontos



def iniciar_hackathon(team):
    """Inicia uma hackathon com rodadas, equipe rival e eventos dinâmicos"""
    
    print("\n" + "=" * 50)
    print("🏆 HACKATHON - PREPARE-SE!")
    print("=" * 50)
    time.sleep(1.0)
    
    # Gerar equipe rival
    equipe_rival = gerar_equipe_rival()
    
    print(f"\n👥 SUAS EQUIPE:")
    for membro in team.membros:
        print(f"   • {membro.nome}")
    
    time.sleep(1.2)
    
    print(f"\n👿 EQUIPE RIVAL:")
    for nome in equipe_rival:
        print(f"   • {nome}")
    
    time.sleep(1.5)
    
    # Iniciar o jogo
    print(f"\n" + "=" * 50)
    print("🎮 INICIANDO AS RODADAS...")
    print("=" * 50)
    time.sleep(1.0)
    
    # Rastreamento de pontos
    pontos = {
        'seu_time': 0,
        'rival': 0
    }
    
    # 4-5 rodadas
    num_rodadas = random.randint(4, 5)
    
    for rodada in range(1, num_rodadas + 1):
        time.sleep(0.8)  # Pausa antes de cada rodada
        
        print(f"\n" + "-" * 50)
        print(f"📍 RODADA {rodada}/{num_rodadas}")
        print(f"   Seu Time: {pontos['seu_time']} pts | Rival: {pontos['rival']} pts")
        print("-" * 50)
        
        time.sleep(1.0)  # Pausa para ler placar
        
        # Escolher evento aleatório
        evento = random.choices(
            [
                lambda: _evento_rodada_bug_nosso(team, pontos),
                lambda: _evento_rodada_bug_rival(pontos),
                lambda: _evento_rodada_genio(team, pontos),
                lambda: _evento_rodada_gambiarra(team, pontos),
                lambda: _evento_rodada_briga_interna(team, pontos),
                lambda: _evento_rodada_confronto_rival(team, pontos),
                lambda: _evento_rodada_caos(pontos),
                lambda: _evento_rodada_maluquice(team, pontos),
                lambda: _evento_rodada_sprint(team, equipe_rival, pontos),
            ],
            weights=[8, 8, 12, 10, 6, 10, 8, 8, 15]
        )[0]
        
        pontos = evento()
    
    # Pausa grande antes do resultado final
    time.sleep(2.0)
    
    # RESULTADO FINAL
    print(f"\n" + "=" * 50)
    print("🏁 RESULTADO FINAL")
    print("=" * 50)
    
    time.sleep(1.0)
    
    print(f"\n   Seu Time: {pontos['seu_time']} pontos")
    print(f"   Rival: {pontos['rival']} pontos")
    
    time.sleep(1.0)
    
    # Fator caos na apresentação
    caos = random.randint(-50, 50)
    pontos['seu_time'] += caos
    
    print(f"\n   🎲 Caos da apresentação: {caos:+d}")
    print(f"   Total Final Seu Time: {pontos['seu_time']} pontos")
    
    time.sleep(1.5)
    
    # Determinar resultado
    if pontos['seu_time'] > pontos['rival']:
        print(f"\n🏆 VITÓRIA ÉPICA!")
        print(f"   Vocês DESTRUÍRAM o rival!")
        print(f"   Diferença: +{pontos['seu_time'] - pontos['rival']} pontos")
        time.sleep(1.0)
        
        for membro in team.membros:
            membro.aura += 20
            membro.programacao += 5
            membro.energia -= 15
            membro.burnout = max(0, membro.burnout - 20)
            print(f"   ✅ {membro.nome}: +20 Aura, +5 Programação, -20 Burnout")
            time.sleep(0.3)
    
    elif pontos['seu_time'] == pontos['rival']:
        print(f"\n⚖️ EMPATE TÉCNICO!")
        print(f"   Vocês igualaram com o rival! Que épico!")
        time.sleep(1.0)
        
        for membro in team.membros:
            membro.aura += 10
            membro.energia -= 10
            membro.burnout = max(0, membro.burnout - 10)
            time.sleep(0.2)
    
    else:
        print(f"\n💀 DERROTA ACACHAPANTE!")
        print(f"   O rival venceu com {pontos['rival'] - pontos['seu_time']} pontos a mais.")
        print(f"   Melhor sorte na próxima...")
        time.sleep(1.0)
        
        for membro in team.membros:
            membro.burnout += 20
            membro.aura -= 10
            membro.sociabilidade -= 5
            membro.energia -= 15
            print(f"   ❌ {membro.nome}: +20 Burnout, -10 Aura")
            time.sleep(0.3)
