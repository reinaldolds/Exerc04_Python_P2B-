'''Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o
algoritmo de seleção.
'''
def ordenacao_por_selecao(vetor):
    n = len(vetor)

    # Percorre todos os elementos do vetor
    for i in range(n):
        indice = i
        for x in range(i+1, n):
            if  vetor[x] < vetor[indice]:
                indice = x
        # Troca os valores dos índices 'i' e 'indice'
        vetor[i], vetor[indice] = vetor[indice], vetor[i]
    
    return vetor


vetor = [64, 25, 12, 22, 11]
print("Vetor original:", vetor)
vetor_ordenado = ordenacao_por_selecao(vetor)
print("Vetor ordenado:", vetor_ordenado)