def inverter_string(string):
    if len(string) <= 1:
        return string
    return string[-1] + inverter_string(string[:-1])

palavra = 'recursao'
resultado = inverter_string(palavra)
print(f"A string '{palavra}' ao contrário vira '{resultado}'.")
