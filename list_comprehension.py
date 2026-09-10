quadrados_impares = [elemento**2 for elemento in range(10) if elemento % 2 != 0]

novo_array = []

for elemento in range (10):
    novo_array.append(elemento**2)

for elemento in novo_array:
    if elemento % 2 != 0:
        print(elemento)