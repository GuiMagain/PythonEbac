# Dado um endereço de IP válido (IPv4), retorne uma versão ajustada desse endereço de IP.
# Um endereço de IP ajustado substitui cada ponto "." por "[.]", para evitar que o endereço de IP seja reconhecido como um link clicável.

# endereço Original = 1.1.1.1
#versão Ajustada = 1[.]1[.]1[.]1

# 1 receber a string com nosso endereço IP

endereco_ip = input("Digite um endereço de IP válido (IPv4): ")

# 2 Fazer a substituiçãpo do ponto por [.]

novo_endereco_IP = ""

for i in endereco_ip:
    if i ==".":
        novo_endereco_ip += "[.]"
    else:
        novo_endereco_ip += i

print("Endereço de IP ajustado:", novo_endereco_ip)