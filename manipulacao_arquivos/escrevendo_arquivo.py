# Trabalhando com o modo de criação e sobreescrita de arquivos
# w-> escreve(substituti) / cria arquivo

arquivo = open("feira.txt", "w")

arquivo.write("Tomate\n")
# arquivo.write("Cebola\n")
# arquivo.write("Tempero\n")
# arquivo.write("Alho\n")

arquivo.close
print("Arquivo escrito")