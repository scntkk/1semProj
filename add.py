import main
def valueError():
    print("Valor inválido! Insira um valor válido.")
    cadastrar()
def cadastrar():
    while True:
        try:
            main.cls()
            print("Cadastro de produtos")
            code = int(input("Insira o código do produto: "))
            print("Código inválido! Insira um código válido.")
            cadastrar()
            custo = float(input("Insira o custo do produto: "))
            if (price < 0):
                print("Preço inválido! Deseja fazer este produto gratuito?")
                choice = input("Sim ou Não: ")
                match choice:
                    case "Sim":
                        price = 0
                    case "Não":
                        cadastrar()
                    case "sim":
                        price = 0
                    case "não":
                        cadastrar()
                    case "nao":
                        cadastrar()
                    case _:
                        print("Escolha inválida!")
                        cadastrar()
            cF = float(input("Insira o custo fixo do produto: "))
            cv = float(input("Insira a comissão de vendas do produto: "))
            imp = float(input("Insira o imposto do produto: "))
        except ValueError:
            valueError()
                
        
    
'''
Solicitar ao usuário o código do produto, o custo do produto, o custo fixo, a comissão de vendas e o imposto.
Finalizar o cadastro do produto.
Quando o usuário finalizar o cadastro, perguntar se deseja cadastrar outro produto.
Se sim, retornar ao início do cadastro.
Se não, retornar ao menu principal.



'''