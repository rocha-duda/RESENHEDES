import time
import sys


def print_lento(texto, delay=0.02):
    """Imprime texto caractere por caractere com delay"""
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def print_pausado(texto, delay_linha=0.3):
    """Imprime texto e aguarda um pouco"""
    print(texto)
    time.sleep(delay_linha)


def esperar_rodada(segundos=1.5):
    """Pausa entre rodadas para o user ler"""
    time.sleep(segundos)


def print_evento(texto, delay_evento=1.0):
    """Imprime um evento e aguarda"""
    print(texto)
    time.sleep(delay_evento)
