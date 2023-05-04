#exercicio 15 do slide de revisão#
'''Escreva um algoritmo para ler dois
valores (considere que não serão lidos
valores iguais) e escrevê-los em ordem
crescente'''

continuar = "sim"

while continuar == "sim":
    valor1 = int(input("Digite o 1º valor: "))
    valor2 = int(input("Digite o 2º valor: "))

    for x in range(1):

        if valor1 == valor2:
            print("numeros iguais, por favor repita a operação e coloque numeros diferentes")
        elif valor1 > valor2:
            print(valor1, valor2)
        else:
            print(valor2, valor1)
    continuar = input("Deseja refazer esse calculo? ").lower()

#Código modificado testando se a estrutura do while suporta o for e o if else: funciona!#