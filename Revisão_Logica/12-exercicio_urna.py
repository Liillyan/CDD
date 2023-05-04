    #exercicio 12 do slide de revisão#
'''Escreva um algoritmo para ler o
número total de eleitores de um
município, o número de votos brancos,
nulos e válidos. Calcular e escrever o
percentual que cada um representa em
relação ao total de eleitores.'''

eleitores = int(input("Quantos eleitores são? "))
branco = int(input("Quantos desses votos foram branco? "))
nulo = int(input("Quantos desses votos foram nulo? "))
valido = int(input("Quantos desses votos foram validos? "))

porc_branco = (branco*100)/eleitores
porc_nulo = (nulo*100)/eleitores
porc_valido = (valido*100)/eleitores
print(f"Desse total temos que {porc_branco}% dos eleitores votaram em branco,"
      f"{porc_nulo}% anularam seu voto, e por fim {porc_valido}% eleitores"
      f" votaram em algum candidato válido totalizando {(porc_valido+porc_nulo+porc_branco)}% das urnas apuradas")

print("------------------------------------------------------------------------------------------------------------")

#Código refatorado em sala de aula#

continua = "sim"

while continua == "sim":

    quant_eleitores = int(input("Digite aqui quantos eleitores participaram dessa eleição: "))
    votos_brancos = int(input("Digite aqui quantos eleitores votaram em branco nessa eleição: "))
    votos_nulos = int(input("Digite aqui quantos eleitores votaram nulo nessa eleição: "))
    votos_validos = int(input("Digite aqui quantos eleitores tiverem seus votos validos nessa eleição: "))

    soma = votos_validos+votos_nulos+votos_brancos

    if soma != quant_eleitores:
        print("Voce digitou alguma quantidade errada")

    else:
        porc_votos_brancos = votos_brancos*100/quant_eleitores
        porc_votos_nulos = votos_nulos * 100 / quant_eleitores
        porc_votos_validos = votos_validos * 100 / quant_eleitores
            
        print(f"De {quant_eleitores} votos, {porc_votos_brancos}% foram votos em branco, "
              f"{votos_nulos}% foram votos nulos e {porc_votos_validos}% foram votos válidos")

    continua = input("Deseja fazer um novo calculo? ").lower()
