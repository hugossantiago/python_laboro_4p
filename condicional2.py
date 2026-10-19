texto = input("Informe um texto qualquer: ")
#print(len(texto)) quantidade de letras

if len(texto) > 10:
    print(texto[:10]) #exibindo o texto até 10 caracteres
else:
    print(texto)