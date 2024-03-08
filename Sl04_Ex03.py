'''
Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem
usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`.'''
def max_element(vet):
    ele_max = vet[0]
    ele_min = vet[0]
    for ele in vet:
        if ele >  ele_max:
            ele_max = ele
        elif ele < ele_min:
            ele_min = ele
    return ele_max, ele_min
v = [9,5,12,7,3]
print("A lista de números: ", v)
print("Elemento Maximo: ",max_element(v)[0])
print("Elemento Minimo: ",max_element(v)[1])