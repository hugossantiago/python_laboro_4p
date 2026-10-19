nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

resultado = (nota1 + nota2 + nota3 + nota4)/4
#print("a média geral é: ", resultado)
"""
comentario
mais de uma linha
"""

"""
if resultado >= 7:
    print("Aprovado, sua média é: ", resultado:.2)
else:
    print("Reprovado sua média é: ", resultado:.2)
"""


if resultado >= 7:
    print(f"Aprovado, sua média é:{resultado:.2}")
elif resultado == 6.7:
    print(f"SIX SEVEN: {resultado}, ta reprovado bobão")
else:
    print(f"Reprovado sua média é:{resultado:.2}")