# Soma de 1 a N: receba um número N e calcule a soma de todos os números de 1 a N.

# Receba um número qualquer

numero_qualquer = int(input("Digite um número para calcular a soma de 1 a N: "))

# Criar a lógica para calcular a soma de 1 a N
# Entender a lógica da soma de 1 a N: 1 + 2 + 3 + ... + N

for i in range(1, int(numero_qualquer) + 1):
    soma += i
print(f"A soma de 1 a {numero_qualquer} é: {soma}")