#exercicio 18 do slide de revisão#
'''18.Escreva um algoritmo que dado um
arrays, retorne um novo array, com os
elementos em ordem invertida.

entrada:
a=[2,5,4,2,8,5,2]

saída
b=[2,5,8,2,4,5,2]'''

B=[]
A=[2,5,4,2,8,5,2]

for x in range(6, -1, -1):
    B.append(A[x])
print(B)