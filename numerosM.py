#Escreva um programa que receba três números e exiba o segundo maior número entre eles.

# precios receber esses números separadamentes, usando o .split() para separar os números e o map() para convertê-los em inteiros.

numero1, numero2, numero3 = map(int, input().split())

#criar uma lógica para ver quem é o segundo maior número entre os três números recebidos.

meu_array = []

meu_array.append(numero1)
meu_array.append(numero2)   
meu_array.append(numero3)

meu_array.sort()

print(meu_array)

#mostrar o resultado do segundo maior número.

print(meu_array[1])

