#exercicio 19 do slide de revisão#
'''
Usando While escreva um algoritmo
que preencha um array A com os 10
primeiros números ímpares, iniciando por
zero

saída
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]'''

cont_impar = 0
A = []
cont = 0

while True:
    if cont % 2!= 0:
        A.append(cont)
        cont_impar+=1
    cont += 1
    if cont_impar == 10:
        break
print(A)

