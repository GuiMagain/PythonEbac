# Dada um array de números unteiros, cada elemento aparece duas vezes, exceto um. Encontre aquele unico elemento.

meu_array = [1, 2, 3, 4, 5, 2, 3, 1, 4]

#1 criar um dicionário para encontrar a quantidade de vezes que cada elemento aparece no array
meu_dicionario = {}

for i in meu_array:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1

#2 encontrar quem é o elemento único que aparece apenas uma vez no array
for chave, valor in meu_dicionario.items():
    if valor == 1:
        print("O elemento único é:", chave) #O elemento único é: 5