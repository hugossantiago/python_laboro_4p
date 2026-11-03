# função sem parametro e sem retorno
def exibirNome():
    nome = input("Qual é o seu nome? ")
    print(f"Olá {nome}, tudo bem? ")

# chamando a função
exibirNome()

# 2º chamando uma função dcom parametro e sem retorno
def somar(num1, num2):
    print(f"A soma é: {num1+num2}")

# chamando a função
somar(2, 10)

# função sem parametro e com retorno
def dobro():
    valor = int(input("Informe um valor numerico: "))
    valor = float(input("Informe um valor numerico: "))
    resposta = valor * 2
    return resposta

# chamando a função
print(f"O dobro é {dobro()}")
