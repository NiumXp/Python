"""
Um programa simples.
Estava fazendo sem ao menos saber usar o while...
"""

valor = input("Digite um número: ")

caracters = len(str(valor))
algarismo = "Algarismo"
número_algarismo = 1
fatiamento = 0

while caracters > 0:
    x = str(valor[fatiamento])
    print("{} {}: {}.".format(algarismo, número_algarismo, x), end='\n')
    caracters -=1
    número_algarismo +=1
    fatiamento +=1
