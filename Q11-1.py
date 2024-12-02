import sys
sys.set_int_max_str_digits(10000) 

def fatorial_iterativo(n):
    resultado = 1  
    for i in range(2, n + 1): 
        resultado *= i 
    return resultado

try:
    print(fatorial_iterativo(1200))
except ValueError as e:
    print("Erro:", e)