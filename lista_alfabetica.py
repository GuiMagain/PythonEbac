#receba uma lista de palavras e ordene-as em ordem alfabética.

array_palavras = [] # criar uma lista vazia para receber as palavras

#receber a lista de palavras

#criar a logica para receber as palavras e inserir na lista

for i in range(1,6): # definir a quantidade de palavras que o usuário deseja inserir, nesse caso 5
    palavra= input(f"Digite a palavra {i}: ")
    array_palavras.append(palavra)

#ordenar a lista em ordem alfabetica

array_palavras.sort() # usar o método sort para ordenar a lista em ordem alfabetica

#printar a lista ordenada

print("As palavras em ordem alfabética são:")
for palavra in array_palavras:
    print(palavra)
