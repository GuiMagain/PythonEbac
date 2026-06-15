# Dado um número em um array de números distintos, no intervalo [0, n], encontre o número que falta nesse array.

meu_array = [0, 1, 2, 4, 5] 

tamanho_array = len(meu_array)
soma_valores_array = sum(meu_array)

soma_total = tamanho_array * (tamanho_array + 1) // 2

numero_faltante = soma_total - soma_valores_array
print("O número que falta nesse array é:", numero_faltante)
