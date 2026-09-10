# Definimos correto o uso de letras maúsculas em uma palavra quando o seguinte caso é válido:

#Todas as letras desta palavra são maiuisculas , como USA

#Dada uma palavra de string, retorne verdadeiro se o uso de maiúsculas está correto 

minha_string = "EUA"

contador = 0

for letra in minha_string:
    if letra.upper():
        contador += 1

print(contador)
print(len(minha_string))

if contador == len(minha_string):
    print("Passou no teste")
else:
    print("Reprovado")