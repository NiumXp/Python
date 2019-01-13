from os import system

class Matrix:
    def gerar(self, x: int, y: int):
        from random import choice
        output = []
        for nada in range(min(x, y), max(x, y)):
            output.append(str(choice([0, 1, '', ' ', ' ', ' ', ' '])))
        return ''.join(output)

    def matrix(self, tempo: int):
        from time import sleep
        while True:
            print(self.gerar(1, 10000))
            sleep(tempo)

system("color 2")
Matrix().matrix(0)
