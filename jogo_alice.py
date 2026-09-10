#você recebe um array de números inteiros positivos. 
#Alice e Bob estão jogando um jogo. 
#No jogo, Alice pode escolher todos os números de um dígito ou todos os números de dois dígitos de números, e os restantes dos números serão escolhidos por Bob.
#Alice ganha se a soma de seus números for estritamente maior que soma dos números de Bob. 
#Retrone verdadeiro se Alice vencer este jogo, caso contrário, retorne falso.

meu_array = [1, 2, 3, 5, 9, 8, 10, 20]
alice = 0 
bob = 0

for numero in meu_array:
    if numero >= 10:
        bob += numero
    else:
        alice += numero

if alice > bob:
    print("Alice venceu o jogo!")
else:
    print("Bob venceu o jogo!")