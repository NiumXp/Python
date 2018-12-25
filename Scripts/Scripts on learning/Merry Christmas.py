"""
Programa feito em base a um desafio proposto por https://github.com/13Ax0
Todos os créditos vão á ele 13Ax0.
"""

from time import sleep

lista = ['2 Turtle Doves', '3 French hens', '4 calling birds', '5 golden rings', '6 geese a-laying', \
         '7 swans a-swimming', '8 maids a-milking', '9 ladies dancing', '10 lords a-leaping', '11 pipers piping',\
         '12 drummers drumming']
#Versos

def repor(x: str):
    if 'st' in x: #1st >> 2nd
        return x.replace('st', 'nd')
    elif 'nd' in x: #2nd >> 3rd
        return x.replace('nd', 'rd')
    elif 'rd' in x: #3rd >> 4th
        return x.replace('rd', 'th')
    elif 'th' in x: #4t >> 5th
        return x.replace('th', 'th')
    else: pass

musica = ['My true love sent to me'] #Versos

day, pos = 1, 'st' #Aqui define o dia (1st)
x = 0 #Será um número para "fatiamento"
#Vai ajudar a pegar os versos na lista la emcima, linha 2

while day != 13: #Enquanto o dia n chegar a ser 13:
    #Vai começar a música
    print(f"On the {day}{pos} day of Christmas") #Começando com o dia.
    for verso in musica: #Vai pegar os versos da lista musica
        print(verso + ',') #E imprimi-los 1 por 1

    #Após acabar esse loop (acima), ele vai terminar o refrão com
    print('1 Partridge in a Pear Tree.\n', "~~"*25)# Este print

    day += 1; pos = repor(pos) #Vai mudar para um novo dia
    #Na primeira passagem, 1st >> 2nd, e assim vai, 2nd >> 3rd...

    if day == 13:
        break #Se o dia chegar a ser 13, o loop vai acabar

    sleep(5) #Vai esperar 5 segundos pra soltar o proximo verso
    musica.insert(1, lista[x]) #Vai passar para o proximo verso
    x += 1 #x vai passar a ser 1, assim pegando outro verso da lista, linha 2


