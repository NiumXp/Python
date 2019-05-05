"""
Script feito em contexto de um desafio. (https://github.com/codehub-discord/desafios/tree/master/02-numeros-felizes)
"""

def sep_ele_sum(number):
    numbers = list(str(number))
    return sum([int(num)**2 for num in numbers])

def verify(number):
    while True:
        if number == 4:
            return False
        elif number == 1:
            return True
        else:
            number = sep_ele_sum(number)

happy_numbers = []
number = 7

while len(happy_numbers) < 20:
    if verify(number):
        happy_numbers.append(number)
    number = number + 1

happy_numbers = ", ".join([str(n) for n in happy_numbers])
print(f" Os vinte primeiros números felizes são:\n\n{happy_numbers}", end=".")
