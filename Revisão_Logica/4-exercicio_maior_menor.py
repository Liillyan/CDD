#exercicio pag 5 do slide de revisão#
'''Crie um algoritmo que receba 3
números e informe qual o maior entre
eles.'''

n1 = int(input("Digite o 1º numero: "))
n2 = int(input("Digite o 2º numero: "))
n3 = int(input("Digite o 3º numero: "))

if n1 > n2 and n1 > n3:
    print("O 1º numero é o maior")
elif n2 > n3 and n2 > n1:
    print("O 2º numero é o maior")
elif n3 > n1 and n3 > n2:
    print("O 3º numero é o maior")
