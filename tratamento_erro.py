texto = "Olá aluno"
print(texto.upper())

try:
    print(texto.calc())

except AttributeError:
    print("Você está tentando executar uma função inválida")


