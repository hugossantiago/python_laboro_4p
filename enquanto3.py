tentativas = 3

while True:
    codigo = input("Informe seu código recebido: ")

    if codigo == "cb450" and tentativas > 0: #codigo correto
        print("Boa! Continue me fazendo feliz.")
        break #parando de repetir a estrutura

    if tentativas > 0: #caso erre a senha o code ira retirar uma de suas tentativas
        tentativas -= 1 #tentativas = tentativas - 1
        print(f"Só mais {tentativas} tentativas") #vai printar o numero de tentativas na tela

    if tentativas <= 0:
        print("Tem mais tentativa não, chefe!")
        break