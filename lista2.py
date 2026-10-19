#Verificando ocorrências de um item na lista

cardapio = ["Refrigerante", "Lanche Mega", "Fritas", "HotDog", "Sobremesa"]

while True: 
    resposta = input("Informe um possível item do cardápio: ")

    if resposta in cardapio:
        print(f"O item {resposta} existe no cardápio")
        break
    else:
        print(f"O item {resposta} não existe no cardápio, tente de novo")