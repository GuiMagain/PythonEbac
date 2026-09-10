#Existem n montanhas seguidas e cada montanha tem uma altura.
#Você recebe uma altura de um array inteiro, onde a altura[i] representa a altura da montanha i e um numero_aleatorio inteiro.
#uma montnha é chamada de estávelse a montanha imediatamente anterior a ela (se existir) tiver uma altura estritamente maior que o numero_aleatorio. 
#Observe que a montanha 0 não é estável. 
#Retorna um array contendo os índices de todas as montanhas estáveis.abs

alturas_das_montanhas = [1, 2 , 3, 4, 5]
numero_aleatorio = 2

meu_array_resultado = []

for posicao in range(1, len(alturas_das_montanhas)):
    if alturas_das_montanhas[posicao - 1] > numero_aleatorio: #-1 se refere a posição anterior do array, ou seja, a montanha imediatamente anterior.
        meu_array_resultado.append(posicao -1)

print(meu_array_resultado)