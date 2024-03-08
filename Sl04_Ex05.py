'''Implemente uma função que aceite um vetor de números inteiros e remova todos os elementos
duplicados, retornando o vetor resultante sem duplicatas.'''
def remove_duplicado(vetor):
    nova_lista = []
    for n in vetor:
        if n  not in nova_lista:
            nova_lista.append(n)
            nova_lista1 = sorted(nova_lista)
    return nova_lista1
vetor = [3, 5, 3, 2, 7, 4, 4, 3, 7]
print("A lista original é:", vetor)
print("A lista sem duplicados: ",remove_duplicado(vetor))