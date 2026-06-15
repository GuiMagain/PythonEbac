# Dado um array de inteiros, um inteteiro sortudo é um inteiro que tem frequência no array igaul o seu valor.

meu_array = [1, 2, 3, 4, 5, 2, 3]

#1 criar um dicionário para encontrar a quantidade de vezes que cada elemento aparece no array

meu_dicionario = {}

for i in meu_array:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1

#2 encontrar quem são os elementos sortudos que aparecem no array com a mesma frequência do seu valor

for chave, valor in meu_dicionario.items():
    if chave == valor:
        print("O elemento sortudo é:", chave) #O elemento sortudo é: 2
