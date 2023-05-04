#exercicio 21 do slide de revisão#
'''Dado o seguinte array [10, 12, 20, 30, 25,
40, 32, 31, 35, 50, 60] . Crie um novo array
com os dados que estão entre os índices 3 e 8'''

B = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
A = []

for x in range(3, 8, 1):
    A.append(B[x])
print(A)
