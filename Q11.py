def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)

try:
    print(fatorial_recursivo(1200))
except RecursionError as e:
    print("Stack Overflow:", e)