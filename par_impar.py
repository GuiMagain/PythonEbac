# Par ou ìmpar: receba um número e exiba se ele é par ou ímpar.

#Receber esse número usando a função input() e converter ele para inteiro usando a função int().

numero = int(input("Digite um número: "))

#verificar se o número é par ou ímpar usando o operador de módulo % para verificar se o número é divisível por 2. Se o resultado for 0, o número é par; caso contrário, é ímpar.s
#printar o resultado usando a função print() para exibir se o número é par ou ímpar.

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
