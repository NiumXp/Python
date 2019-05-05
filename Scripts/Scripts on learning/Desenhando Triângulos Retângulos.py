"""
Script feito em contexto de um desafio. (https://github.com/codehub-discord/desafios/tree/master/06-desenhando-triangulos#exemplos)
"""

from os import system, name
from time import sleep

def clear():
    command = "cls" if name == "nt" else "clear"
    return system(command)

altura = int(input("Altura do triângulo: "))
clear()
print("Triângulo com sequência numérica:\n")
for number in range(0, altura):
    print("".join([str(i) for i in list(range(1, number + 2))]))

sleep(2); clear()
print("Triângulo totalmente sólido:\n")
for number in range(1, altura + 1):
    print("*" * number)


sleep(2); clear()

lista = ["*"]
print("Triângulo somente com uma borda:\n")
for number in range(1, altura + 1):
    print("".join(lista))
    if len(lista) == 1:
        lista.append("*")
    elif number == altura - 1:
        lista = ["*" * (number + 1)]
    else:
        lista.insert(1, " ")
