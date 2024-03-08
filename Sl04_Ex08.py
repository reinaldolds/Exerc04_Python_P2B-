'''Crie uma função que receba um vetor de números inteiros e retorne a mediana, ou seja, o valor do
meio quando o vetor é ordenado. Certifique-se de que sua função funcione para vetores com um
número ímpar de elementos.'''
def mediana(vetor):
    vetor_ordenado = sorted(vetor)
    tamanho = len(vetor_ordenado)
    
    if tamanho % 2 != 0:
        indice_mediana = tamanho // 2
        return vetor_ordenado[indice_mediana]
    
    else:
        indice_mediana1 = tamanho // 2 - 1
        indice_mediana2 = tamanho // 2
        valor_mediana1 = vetor_ordenado[indice_mediana1]
        valor_mediana2 = vetor_ordenado[indice_mediana2]
        return (valor_mediana1 + valor_mediana2) / 2

vetor1 = [5, 2, 8, 3, 2, 10, 8, 6]
vetor2 = [7, 4, 1, 9, 6, 3, 5]

mediana_vetor1 = mediana(vetor1)
mediana_vetor2 = mediana(vetor2)
print("Lista 1:", vetor1)
print("Lista 2:", vetor2)
print("Mediana da lista 1:", mediana_vetor1)
print("Mediana da lista 2:", mediana_vetor2)
