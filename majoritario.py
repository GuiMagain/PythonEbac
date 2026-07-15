#Dado um array de tamamho n retorne o elemento majoritario
#O elemento majoritario é aquele que aparece mais de [n/2] vezes.
# você pode assumir que o elemento majoritario sempre existe no array.

array = [3, 2, 3]

n = len(array)

item_majoritario = n/2

dicionario = {}

for item in array:
    if item not in dicionario:
        dicionario[item] = 1
    else:
        dicionario[item] += 1 

for chave, valor in dicionario.items():
    if valor >= item_majoritario:
        print(chave)