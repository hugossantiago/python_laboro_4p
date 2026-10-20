"""
Dicionario:
Chave: Valor -> Item

Chave -> key
Valor -> value
Item -> item

"""
contatos = {"joão": 123, "maria": 456, "josé": 789} 
print(contatos)

#EXIBINDO APENAS AS CHAVES 
for chave in contatos.keys():
    print(chave)

#EXIBINDO APENAS OS VALORES
for valor in contatos.values():
    print(valor)

#EXIBINDO O ITEM, TANTO CHAVE QUANTO VALOR
for chave, valor in contatos.items():
    print(f"{chave} : {valor}")