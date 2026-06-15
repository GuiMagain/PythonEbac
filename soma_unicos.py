#Você recebe um array de números inteiros 
#Os elementos únicos de um array são aqueles que aparecem exatamente uma vez no array.
#retorne a soma de todos os elementos únicos que aparecem uma vez no array.

me_array = [1, 2, 3, 4, 5, 2, 3]

#1 criar um dicionário para encontrar a quantidade de vezes que cada elemento aparece no array

meu_dicionario = {}

for i in me_array:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1

#2 encontrar quem são os elementos únicos que aparecem apenas uma vez no array

soma_unicos = sum(valor for valor, quantidade in meu_dicionario.items() if quantidade == 1)
print(soma_unicos) #A soma dos elementos únicos é 10 (1 + 4 + 5)