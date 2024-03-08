'''Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, em seguida, conte
quantos números pares e quantos números ímpares existem no vetor ordenado.'''
def contar_pares_impares(vetor):
    vetor_ordenado = sorted(vetor, reverse=True)
    pares = 0
    impares = 0
    for numero in vetor_ordenado:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

vetor = [5, 2, 1, 3, 2, 9, 8, 6]
num_pares, num_impares = contar_pares_impares(vetor)

print("Vetor ordenado em ordem decrescente:", vetor)
print("Quantidade de números pares:", num_pares)
print("Quantidade de números ímpares:", num_impares)
