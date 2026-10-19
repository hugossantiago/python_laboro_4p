mercearia = ["Frutas", "Verduras", "Bebidas", "Carnes", "Água Sanitária"]

print(type(mercearia))
print(mercearia)

mercearia[4] = "Feijão"
print(mercearia)

#Exibindo a lista completa
for item in mercearia:
    print(item)

#Inserindo item no final da lista
mercearia.append("Batata")
print(mercearia)

#Inserindo item em qualquer lugar da lista 
mercearia.insert(2, "Açúcar Mascavo")
print(mercearia)

#Removendo o último itens da lista
mercearia.pop()
print(mercearia)

#Removendo qualquer item da lista
mercearia.pop(4)#remove o item de acordo com o indice.
print(mercearia)

mercearia.remove("Bebidas")
print(mercearia)
