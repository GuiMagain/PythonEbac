# Dado um array inteiro não classificado meu_array. 
# Retorne o menor número inteiro positivo que não está em meu_array.
from collections import Counter

meu_array = [3, 4, 1]

#Esse número é maior do que ZERO
#Ele NÃO é decimal
#Ele é o menor número inteiro positivo que não está presente no array.

contador = 1 

meu_dicionario =  {}

meu_dicionario = Counter(meu_array)

while True:
    if contador not in meu_dicionario:
        contador += 1
    else:
        print(contador)
        break
