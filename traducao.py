#A tradução da língua berland para a língua birland são muito semelhantes.
# Uma palavra berlandesa difere um pouco de uma palavra birlandesa com o mesmo significado.
# É escrita e pronunciada inversamente.
# Por exemplo a palavra berlandesa "code" corresponde a uma palavra birlandesa "edoc".
#Vasya traduziu a palavra s de berlandish para birlandish como t.
# Ajude Vasya a determinar se a tradução está correta.

primeira_string = "code"
segunda_string = "edoc"

if primeira_string == segunda_string[::-1]:
    print("sim, foi traduzido corretamente")
else:
    print("não, foi traduzido incorretamente")