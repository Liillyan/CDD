#exercicio 17 do slide de revisão#

'''17.As maçãs custam R$ 1,30 cada se forem
compradas menos de uma dúzia, e R$ 1,00
se forem compradas pelo menos 12. Escreva um
programa que leia o número de maçãs
compradas, calcule e
escreva o custo total da compra.'''

compras = int(input("Digite a quantidade de maçãs que deseja adquirir: "))

if compras > 12:
    total = compras*1.00
    print(f"Cada maça saira por R$1,00 totalizando R${total}")
else:
    total2 = compras * 1.30
    print(f"Cada maça saira por R$1,30 totalizando R${total2}")
