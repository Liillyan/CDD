#exercicio 9 do slide de revisão#
'''Faça um algoritmo que receba 4
números e realize a soma deles e a
média entre eles. e mostre os
resultados.'''

n1 = int(input("Digite o 1º numero: "))
n2 = int(input("Digite o 2º numero: "))
n3 = int(input("Digite o 3º numero: "))
n4 = int(input("Digite o 4º numero: "))

soma = (n1+n2+n3+n4)
media = soma/4
print(f"A media desses 4 numeros é {media}")

#mesmo exercicio feito com for#

soma = 0

for x in range(1, 5):
  num = int(input(f"Digite aqui o {[x]} numero: "))
  soma=soma+num
print(f" A media dos 4 numeros digitados é {soma/4})
