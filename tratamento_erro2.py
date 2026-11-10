try:

    resposta = int(input("Informe um valor numérico: "))
    
    print(f"O número informado é: {resposta}")
    
except ValueError as erro:
    print(f"Erro de valor: {erro}")
    print("Você precisa informar apenas valores numéricos")

finally: #esse trecho sempre será executado
    print("\nObrigado por usar o sistema\n")



