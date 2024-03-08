'''Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro que
serve como chave para realizar a ordenação crescente ou decrescente.'''
def ordenar_vetor(vetor):
    vetor.sort()
    return vetor

# Exemplo de uso:
vetor = [10, 25, 12, 22, 11]
print("Vetor original:", vetor)
vetor_ordenado = ordenar_vetor(vetor)
print("Vetor ordenado:", vetor_ordenado)
 
