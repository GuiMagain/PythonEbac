class animal:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "O animal emite um som genérico."

class cachorro(animal):
    def emitir_som(self):
        return "O cachorro late: Au Au!"

class gato(animal):
    def emitir_som(self):
        return "O gato mia: Miau!"

if __name__ == "__main__":
    meu_cachorro = cachorro("Bud", idade=5)
    meu_gato = gato("Morfeu", idade=3)

    print(meu_cachorro.emitir_som())
    print(meu_gato.emitir_som())