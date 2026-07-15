#Dado um array inteiro, retornew verdadeiro se algum valor aparecer pelo menos duas vezes no array
#Retorne falso se cada elemento for distinto

array = [1,1,1,3,3,4,3,2,2]

dicionario = {}

for numero in array:
    if numero not in dicionario:
        dicionario[numero] = 1
    else:
        dicionario[numero] += 1

for chave, valor in dicionario.items():
    if valor >= 2:
        print(True)
    else:
        print(False)