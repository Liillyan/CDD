#exercicio 20 do slide de revisão#
'''Escreva um algoritmo que receba do
usuário 10 números e mostre:
1. todos os números ímpares;
2. todos os números pares;
3. todos os números positivos;
4. todos os números negativos;
5. todos os zeros que aparecem no array'''

A = []

for x in range(10):
    A.append(int(input("Digite um numero: ")))
print(A)

for y in range(10):
    if A[y] % 2!=0:
        print(f"impares: {A[y]}")
for w in range(10):
    if A[w] %2 ==0:
        print(f"pares: {A[w]}")
for k in range(10):
    if A[k] >0:
        print(f"numeros positivos: {A[k]}")
for t in range(10):
    if A[t] <0:
        print(f"numeros negativos: {A[t]}")
for u in range(10):
    if A[u] ==0:
        print(f"todos os zeros: {A[u]}")