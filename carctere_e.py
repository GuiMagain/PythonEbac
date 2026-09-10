# Você recebe um array indexado em 0 de palavras de strings e um caractere x.
# Retorne um array de índices que representam as palavras que contêm o caractere x.

words = ["apple", "banana", "cherry", "date", "elderberry"]
string = "e"
resultado = []

for posicao, palavra in enumerate(words):
    if string in palavra:
        resultado.append(posicao)

print(resultado)
