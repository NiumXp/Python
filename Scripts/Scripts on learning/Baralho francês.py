"""
Script feito em contexto de um desafio. (https://github.com/codehub-discord/desafios/tree/master/01-baralho-frances)
"""

from random import randint
from os import system, name
from time import sleep

naipes = ["♣", "♦", "♥", "♠"]
tipos = ["Ás", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valete", "Dama", "Rei"]

baralho = []

def clear():
    command = "cls" if name == "nt" else "clear"
    return system(command)

def shuffle(object):
    output = []
    for item in object:
        output.insert(randint(0, len(object)), item)
    return output

def print_cards(card_list):
    cards = []
    for index in range(0, 52, 13): # 0 -> 13 -: 26 -> 39
        # 52 tem o divisor 4, assim posso mostrar 4 linhas de cartas.
        # Se o stop fosse 53 aparecia uma lista vazia no final.
        for card in card_list[index: index + 13]:
            cards.append("{: >8}".format(card))

    for index in range(0, 52, 13): # Mesma lógica acima.
        print(" ".join(cards[index: index + 13]))

#Gerando baralho.
for naipe in naipes:
    for tipo in tipos:
        baralho.append(tipo + naipe)

decisao = "nada aqui"
while decisao not in [0, 1, 2, 3]:
    print("""
 O que você deseja fazer?

 [0] - Limpar o terminal.
 [1] - Ver o baralho.
 [2] - Embaralhar o baralho.
 [3] - Sair.
""")
    decisao = int(input(" > "))
    if decisao == 0:
        clear()
        print("\n Você optou por limpar o terminal.\n")
        decisao = "nada aqui também" # Nescessário por conta do continue abaixo e condição do laço.
        continue
    elif decisao == 1:
        clear()
        print(" Limpei o terminal para termos uma visualização melhor do baralho.\n")
        print_cards(baralho)
        print("\n Você optou por ver o baralho.\n")
    elif decisao == 2:
        baralho = shuffle(baralho)
        print("\n Você optou por embaralhar o baralho.\n")
    else:
        exit()
    decisao = "nada aqui também" # Nescessário por conta da condição do laço.
    sleep(3) # Só pra deixar dinâmico.
