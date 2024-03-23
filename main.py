import os, mysql.connector, add
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def main():
    while True:     
        print("Bem-vindo!")
        print("Selecione uma ação: ")
        print("[1] Adicionar novo produto")
        print("[2] Listar produtos")
        print("[3] Sair")
        choice = input("Insira sua escolha: ")
        match choice:
            case "1":
                add.cadastrar()
            case "2":
                print("Não implementado!")
            case "3":
                exit()
            case _:
                print("Ação inválida!")
                main()
if (__name__ == "__main__"):
    main()