#questão do jogo de xadrez#

hora_inicio = int(input("Digite a hora que o jogo começou: "))
hora_fim = int(input("Digite a hora que o jogo terminou: "))

''' considere que a hora de inicio sera menor que a hora do fim quando termina no mesmo dia, quando for o contrario sera pq terminou no dia seguinte'''

#resolução de uma das questões da revisão#
B = []
A=[2,5,8,4,7,5,2]

for x in range(6, -1, -1):
    B.append(A[x])
#   B[6-x]=A[x]
