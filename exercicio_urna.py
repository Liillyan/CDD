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