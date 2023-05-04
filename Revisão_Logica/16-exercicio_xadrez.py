#exercicio 16 do slide de revisão#
'''Escreva um algoritmo para ler a hora de
início e a hora de fim de um jogo de Xadrez
(considere apenas horas inteiras, sem os
minutos) e calcule a duração do jogo em
horas, sabendo-se que o tempo máximo de
duração do jogo é de 24 horas e que o jogo
pode iniciar em um dia e terminar no dia
seguinte'''

''' considere que a hora de inicio sera menor que a hora do fim quando termina no mesmo dia,
 quando for o contrario sera pq terminou no dia seguinte'''

hora_inicio = int(input("Digite a hora que o jogo começou: "))
hora_fim = int(input("Digite a hora que o jogo terminou: "))

if hora_inicio < hora_fim:
    duracao = hora_fim-hora_inicio
    print(f"A duração do jogo foi de {duracao}")
else:
    duracao = 24-hora_inicio+hora_fim
    print(f"A duração do jogo foi de {duracao}")
