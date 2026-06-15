# Dada um array de números inteiros, reotorne a soma do menor e do maior número presente nesse array.

meu_array = [1, 18, 55, 48, 49, 62]

#ordenar o array do menor para o maior

meu_array.sort()

#fazer a soma do menor e do maior número presente nesse array

primeiro_valor = meu_array[0]
ultimo_valor = meu_array[-1]

print("A soma do menor e do maior número presente nesse array é:", primeiro_valor + ultimo_valor) #A soma do menor e do maior número presente nesse array é: 63 (1 + 62)
