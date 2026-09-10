# Receba um número de 1 a 10 e exiba a tabuada desse número.

# Receber o número para poder mostra a tabuada

numero_tabuada= float(input("Digite um número de 1 a 10 para mostrar a tabuada: "))

# Criar a lógica para mostrar a tuabuada

for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")