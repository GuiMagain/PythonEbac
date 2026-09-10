# Antony gosta de jogar xadrez, assim como seu amigo Daniel.
# Depois de terem jogado n jogos consecutivos, para cada jogo sabe-se quem foi o vencedor - Antony ou Daniel.
# Nenhum dos jogos terminou empatado.
# Agora Antony se pergunta quem gahou mais jogos ele ou o Daniel?

quantidade_de_jogos = 6
vencedores_cada_jogo = "Antony Daniel Antony Daniel Antony Antony"

quantiddade_de_vitorias_antony = vencedores_cada_jogo.split().count("Antony") #split() -> separa a string em uma lista de palavras, usando o espaço como delimitador
quantiddade_de_vitorias_daniel = vencedores_cada_jogo.split().count("Daniel") #count() -> conta quantas vezes a palavra "Daniel" aparece na lista

if quantiddade_de_vitorias_antony > quantiddade_de_vitorias_daniel:
    print("Antony ganhou mais jogos")
else:
    print("Daniel ganhou mais jogos")