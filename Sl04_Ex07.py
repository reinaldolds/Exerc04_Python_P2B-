'''Crie uma função que aceite um vetor de números inteiros e retorne o terceiro maior número.
Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.'''
def terceiro_maior(vetor):
    vetor_ordenado = sorted(set(vetor), reverse=True)

    if len(vetor_ordenado) < 3:
        return None  
    return vetor_ordenado[2]

vetor = [5, 2, 1, 3, 2, 22, 8, 6]
terceiro_maior_numero = terceiro_maior(vetor)

print("O terceiro maior número é:", terceiro_maior_numero)
