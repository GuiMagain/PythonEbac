#Dado um array. definimos uma soma acumulada de um array como runningSum[i] = sum(array[0]+array[i]).
#retorne a soma acumulada de array.
#Explicação: a soma acumulada é obtida da seguinte forma: [1, 1+2, 1+2+3, 1+2+3+4].

array = [1,2,3,4]
resultado_array = []

contador = 0

for numero in array:
    contador += numero
    resultado_array.append(contador)

print(resultado_array)