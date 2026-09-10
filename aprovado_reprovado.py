# - Aprovado, reprovado ou recuperação:
# Receba a média de um aluno e diga se ele foi aprovado (média 7 ou superior)
# Em recuperação (5 < média <7) ou
#reprovado (média 5 ou inferior).

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"O aluno foi aprovado com média {media:.2f}.")
elif 5 <= media < 7:
    print(f"O aluno está em recuperação com média {media:.2f}.")
else:
    print(f"O aluno foi reprovado com média {media:.2f}.")