class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo!")

class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} está latindo: ruf ruf!")

meu_cachorrinho = Cachorro ("Bud")

meu_cachorrinho.comer()
meu_cachorrinho.latir()