def qtd_caracteres(string, caracteres):
    if not string:
        return 0
    return (1 if string[0] == caracteres else 0) + qtd_caracteres(string[1:], caracteres)

palavra = 'banana'
letra = 'a'
resultado = qtd_caracteres(palavra, letra)
print(f"A quantidade de vezes que '{letra}' aparece em '{palavra}' é {resultado}.")