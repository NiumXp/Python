"""
Programa aonde ele me volta números perfeitos.
Estava aprendendo a usar o "for" e o "range()"
"""

n = 0
n1 = 10000
pn = list()
while n < n1:
	teste = 0
	for i in range(1, n):
		if n % i == 0:
			teste=teste+i
	if teste == n:
		#print (n, 'é um número perfeito!')
		pn.append(n)
	n +=1
for elementos in pn:
	print(elementos, end=', ')
print('são números perfeitos!')
