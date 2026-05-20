import random
from .evento_resenha import evento_resenha
from .evento_bug import evento_bug
from .evento_gambiarra import evento_gambiarra
from .evento_fofoca import evento_fofoca
from .evento_trairagem import evento_trairagem
from .evento_colapso import evento_colapso_mental
from .evento_academia import evento_academia


def gerar_evento(team):
    """Gera um evento aleatório baseado no estado do time"""
    
    membros = team.membros

    if len(membros) < 2:
        return

    evento_pool = []

    # =========================
    # EVENTOS BASE
    # =========================

    evento_pool.extend([
        lambda: evento_resenha(team),
        lambda: evento_bug(team),
        lambda: evento_gambiarra(team)
    ])

    # =========================
    # EVENTOS CONTEXTUAIS
    # =========================

    for membro in membros:

        # burnout
        if membro.burnout >= 70:
            evento_pool.append(lambda: evento_colapso_mental(team))

        # fofoqueiro
        if "fofoqueiro" in membro.traits:
            evento_pool.append(lambda: evento_fofoca(team))

        # falsidade
        if "falsidade" in membro.traits:
            evento_pool.append(lambda: evento_trairagem(team))

        # maromba
        if "maromba" in membro.traits:
            evento_pool.append(lambda: evento_academia(team))

    evento = random.choice(evento_pool)
    evento()
