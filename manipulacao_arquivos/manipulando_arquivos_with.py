# Criando um novo arquivo 

#Criando arquivo com suporte a caracteres especiais
with open("comida.txt", "w", encoding="utf-8") as comida:
    comida.write("Hot Dog\n")
    comida.write("Coxão Assado\n")
    comida.write("Bolo de Milho\n")
    comida.write("Rabada cozida\n")
    comida.write("Salada\n")
    
# Consultando arquivo
with open("comida.txt", "r", encoding="utf-8") as comida:
    print(comida.read())
    