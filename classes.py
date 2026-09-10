# As classes funcionam como moldes, veja a seguir, o molde de pokemon, onde temos um pokemon com vários atributos

#A classe é o molde que vamos usar para poder contruir as coisas

class MoldePokemon:
    def __init__(self, nome, altura, peso, hp, ataque, tipo):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.hp = hp
        self.ataque = ataque
        self.tipo = tipo

    def mostrar_nome_pokemon(self):
            print(f"O nome do meu Pokémon é: {self.nome}")

    def mostrar_altura_pokemon(self):
         print(f"A altura do Pokémon é: {self.altura} ")

    def mostrar_peso_pokemon(self):
         print(f"O peso do Pokémon é: {self.peso} ")

    def mostrar_hp_pokemon(self):
         print(f"o hp do Pokémon é: {self.hp} ")

    def mostrar_ataque_pokemon(self):
         print(f"O ataque do Pokémon é: {self.ataque} ")

    def mostrar_tipo_pokemon(self):
         print(f"O tipo do Pokémon é: {self.tipo} ")



# Por enquanto temos só o molde, a seguir vamos dar os valores e mostrar os valores do molde

Pikachu = MoldePokemon("Pikachu", 50, 15, 400, "Choque do Trovão", "Elétrico")

Pikachu.mostrar_nome_pokemon()
Pikachu.mostrar_altura_pokemon()
Pikachu.mostrar_peso_pokemon()
Pikachu.mostrar_hp_pokemon()
Pikachu.mostrar_ataque_pokemon()
Pikachu.mostrar_tipo_pokemon()