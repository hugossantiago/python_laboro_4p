agenda = dict()# Criando um dicionário vazio

#FUNÇÃO MENU
def menu():
    print("\nAgenda Eletrônica\n")
    print("1 - Inserir")
    print("2 - Excluir")
    print("3 - Consultar")
    print("4 - Sair")
    
#----------------------------------------------------------
#FUNÇÃO INSERIR
def inserir():
    try:
        nome = input("Informe o nome do contato: ")
        agenda[nome] = int(input(f"Qual o número de {nome}: "))
            
        print("Contato inserido com sucesso!")
        print(agenda)
        
    except Exception:
        print("Operação inválida. Contato não salvo!")
    
#FUNÇÃO EXCLUIR
def excluir(valor):
    if valor in agenda:
        del agenda[valor]
        print(f"O contato {valor} foi excluído com sucesso")
        print(agenda)
    else: 
        print(f"O contato {valor} não existe na agenda")
        print("Contato não excluído")
      
#FUNÇÃO CONSULTAR
def consultar():
    for chave, valor in agenda.items():
        print(f"{chave}: {valor}")
#--------------------------------------------------------------

while True:
    menu()
    escolha = input("Qual sua escolha?")
    if escolha == "1": 
        inserir()
        
    elif escolha == "2":
        resposta = input("Informe aqui o contato você deseja excluir: ")
        excluir(resposta)
       
    elif escolha == "3":
        consultar()
        
    elif escolha == "4": 
        break
    else: 
        print("Opção inválida")
        input("\nAperte qualquer tecla para continuar...")