meu_array = [1,2,3,4,5,5,6,7,8,9,9]

#chave - valor

#Numero dentro do array sendo a chave
#A quantidade de vezez que ele aparece sendo valor

meu_dicionario = {
    #1 : 1,
    #2 : 1,
    #3 : 1,
    #4 : 1, 
    #5 : 2, 
    #6 : 1,
    #7 : 1,
    #8 : 1,
    #9 : 2
}

for numero in meu_array:
    if numero not in meu_dicionario:
        meu_dicionario[numero] = 1
    else:
        meu_dicionario[numero] += 1 

meu_array_resultado = []

for chave, valor in meu_dicionario.items():
    if valor == 2:
        meu_array_resultado.append(chave)

print(meu_array_resultado)