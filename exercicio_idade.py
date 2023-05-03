#exercicio pag 4 do slide de revisão#
'''Crie um algoritmo que leia a idade
de uma pessoa e diga em qual ano ela
nasceu'''

idade = int(input("Digite aqui sua idade: "))
ano_atual = int(input("Digite aqui o ultimo ano que voce fez aniversario: "))

x = (ano_atual-idade)

print(f"O seu ano de nascimento é: {x}")