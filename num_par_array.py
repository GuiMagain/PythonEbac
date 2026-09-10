# Dado um array de números inteioros, reotrne quantos números pares existem nesse array.
# nums = [12,345,2,6,7896] -> esses va~lores sao numeros inteiros
# novo_array = ["12","345","2","6","7896"] -> esses valores sao strings

# 1 criar um novo array de strings que vai ter os mesmos valores do primeir array mas convertidos para string

nums = ["12","345","2","6","7896"]

# 2 fazer um loop para contar quantos numeros pares existem nesse novo array de string
count = 0
for i in nums:
    if len(i) %2 == 0:
        print(i, "é um número par.")
        count += 1

# fazer a contagem de numeros pares e imprimir o resultado

print("Quantidade de números pares:", count)