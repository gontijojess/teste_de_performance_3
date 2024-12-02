def soma_numeros(nums):
    if not nums:
        return 0
    return nums[0] + soma_numeros(nums[1:])

array_numeros = [1, 2, 3, 4]
resultado = soma_numeros(array_numeros)
print(f"A soma dos elementos desse array é {resultado}")
