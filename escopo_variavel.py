idade = 30 # esta variável tem escopo/visibilidade global

def mensagem():
    #idade = 50  # esta variável tem visibilidade local
    
    global idade #Estamos informando que a variavel idade, que é global, também funcionará dentro da função.
    
    idade = idade + 20
    
    print(f"Olá, sua idade é {idade}")
    
mensagem() 

print(f"Sabemos que sua idade é {idade}")
    