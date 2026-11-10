def processar_dados(valor1, valor2):
    try:
        soma = valor1 + valor2
        divisao = valor1 / valor2
        decimal = float(valor1 * valor2)
        
        print(f"A soma é: {soma}")
        print(f"A divisão é: {divisao}")
        print(f"O valor convertido para decimal é: {decimal}")
        
    except ValueError as erro:
        print("Você precisa informar valores numéricos")
        
    except ZeroDivisionError as erro:
        print("Tentando fazer divisão por zero, né, safado?")
        
    except Exception as erro:# O Exception trata errs de forma genérica, caso você não saiba qual erro ocorre
        print(f"Um erro aconteceu: {erro}")
        
                
#CHAMANDO A FUNÇÃO 
processar_dados(10, 2)
processar_dados(10, 0)# vai dar merda KDMSAKMDASKSADAM
processar_dados("oi", 0)



