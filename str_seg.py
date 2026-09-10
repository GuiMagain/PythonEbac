#Dada uma string minha_string, rertorne o  numero de segmwntos na string.

#um segmentop é definido como uma sequência contínua de caracteres que não contém espaços.

minha_string = "Hello World !!"

meu_array = minha_string.split() # Usa o método split() para dividir a string em uma lista de segmentos, usando o espaço como delimitador

print(len(meu_array)) # Imprime o número de segmentos na lista usando a função len() para contar os elementos