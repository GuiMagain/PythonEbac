def counter_function():
    count = 0
    while True:
        yield count
        count += 1

counter = counter_function()
print(next(counter))  # Output: 0
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2

# O código acima define uma função geradora chamada `counter_function` que utiliza a palavra-chave `yield` para criar um gerador.
# Yield é uma palavra-chave em Python que é usada para criar geradores. Um gerador é um tipo especial de iterador que pode ser pausado e retomado.