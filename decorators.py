def meu_decorator(func):
    def wrapper():
        print("Antes da execução da função.")
        func()
        print("Depois da execução da função.")
    return wrapper

@meu_decorator
def minha_funcao():
    print("Esta é a minha função.")

minha_funcao()