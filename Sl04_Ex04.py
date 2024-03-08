'''Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número.
Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.'''
def segundo_menor(vetor):
    # Remova duplicatas e ordene o vetor
    vetor_sem_duplicatas = sorted(set(vetor))

    # Verifica se há menos de dois elementos únicos no vetor
    if len(vetor_sem_duplicatas) < 2:
        return None  # Não há segundo menor número

    # Retorna o segundo elemento após o menor elemento
    return vetor_sem_duplicatas[1]

vetor = [5, 2, 8, 3, 2, 9, 8, 6]
segundo_menor_numero = segundo_menor(vetor)

print("O segundo menor número é:", segundo_menor_numero)
