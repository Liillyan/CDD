#exercicio 9 e 10 do slide de revisão#
''''Faça um Algoritmo que receba um
número inteiro e mostre o seu
antecessor.'''

num = int(input("Digite um numero e será printado seu antecessor: "))
print(f" o antecessor de {num} é {(num-1)}")

print("---------------")

'''Faça um Algoritmo que receba um
número inteiro e mostre o seu
sucessor.'''

num = int(input("Digite um numero e será printado seu sucessor: "))
print(f" o sucessor de {num} é {(num+1)}")

#CÓDIGO ACIMA FEITO EM CASA ENQUANTO QUE O CÓDIGO ABAIXO FOI REFEITO EM SALA#

'''Durante a aula foi questionado que o usuario poderia digitar um numero negativo,
então foi refeito o código'''

n = int(input("Digite aqui um numero e direi seu antecessor: "))

if n >= 0:
    print(f"O antecessor de {n} é {n-1}")
else:
    print(f"O antecessor de {n} é {n-(-1)}")

print("---------------------------------------------------------")

num = int(input("Digite aqui um numero e direi seu sucessor: "))

if num <= 0:
    print(f"O sucessor de {num} é {num+1}")
else:
    print(f"O sucessor de {num} é {num - (+1)}")
