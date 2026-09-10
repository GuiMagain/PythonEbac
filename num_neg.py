# Dado um número inteiro não negativo meu_numero,
# Retorne a raiz quadrada de meu-numero arredondada para o numero inteiro mais próximo.
# O número inteiro retornado também deve ser não negativo.

import math  # Importa a biblioteca math para usar a função sqrt (raiz quadrada)

meu_numero = 144

resultado = math.sqrt(meu_numero) # Calcula a raiz quadrada de meu_numero usando a função sqrt da biblioteca math

print(round(resultado))