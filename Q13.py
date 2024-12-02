def is_palindromo(palavra):
    if len(palavra) <= 1:
        return True
    if palavra[0] != palavra[-1]:
        return False
    return is_palindromo(palavra[1:-1])

palavras = ["mirim", "ovo", "arara", "teste"]
for p in palavras:
    if (is_palindromo(p)):
        print(f"A palavra '{p}' é um palíndromo")
    else:
        print(f"A palavra '{p}' não é um palíndromo")