#receba um número e verifique se ele é um palíndromo (uma palavra ou número que pode ser lido da mesma forma de trás para frente).

# Receber o número para verificar se é um palíndromo inteiro

numero = int(input("Digite um número: "))

#converter o número para string para poder verificar se é um palíndromo

numero_str = str(numero)

#retornar se é ou não um palíndromo

if numero_str == numero_str[::-1]:
    print(" é um palíndromo.")
else:
    print("não é um palíndromo.")