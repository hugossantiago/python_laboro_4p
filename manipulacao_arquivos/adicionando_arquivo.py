# Trabalhando com o modo de adição de itens
# a -> cria arquivo, caso não exista, e adiciona itens no final 

#Abrindo o arquivo em modo de escrita
arquivo = open("frutas.txt", "a")

#print(arquivo.readable())

#Adicionando itens no arquivo
arquivo.write("\nMorango\n")
arquivo.write("Banana\n")

arquivo.close()
