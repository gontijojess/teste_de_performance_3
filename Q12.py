def soma_recursiva(array):
    if not array:
        return 0

    return array[0] + soma_recursiva(array[1:])

array_numeros = [1, 2, 3, 4, 5, 6]
resultado = soma_recursiva(array_numeros)
print(f"A soma dos elementos da lista usando recursividade: {resultado}")