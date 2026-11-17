# Vamos abrir um arquivo
# r-> modo de leitura

# Abrindo o arquivo em modo leitura
arquivo = open("frutas.txt", "r")

# Verificando se o arquivo pode ser lido
print(arquivo.readable())

#Lendo o conteúdo do arquivo
#print(arquivo.read())

#Lendo várias linhas
arquivo.readline()
arquivo.readline()
resultado = arquivo.readline() #exibindo o 3° item
print(resultado)

# Criando uma lista com os itens 
print(arquivo.readlines())

arquivo.close()#Fechar o arquivo 