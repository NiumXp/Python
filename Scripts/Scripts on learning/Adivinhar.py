"""
Simples programa de adivinhar um int(input())
Estava aprendendo while...
"""

from random import randint

tentativas, numero_aleatório, numero_do_jogador = 0, randint(1, 9), 0

while numero_do_jogador != numero_aleatório:
    if numero_do_jogador == 0:
        numero_do_jogador = int(input("Digite um número!! "))
    else:
    	numero_do_jogador = int(input("\nDigite outro número!! "))
    tentativas += 1
    if numero_do_jogador == numero_aleatório:
        if tentativas == 1:
            print(f"\nVocê tentou advinhar {tentativas} vez!!")
        else:
            print(f"\nVocê tentou advinhar {tentativas} vezes!!")
    elif numero_do_jogador > numero_aleatório:
    	print(f"\nDigite um valor menor do que {numero_do_jogador}!!")
    elif numero_do_jogador < numero_aleatório:
    	print(f"\nDigite um valor maior do que {numero_do_jogador}!!")

