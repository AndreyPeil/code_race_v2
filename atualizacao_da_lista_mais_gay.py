def mostrar_lista(opcao):
    lista = {
        1: "Andrey Baitolão",
        2: "Otavio GAYZAO",
        3: "Lucas VIADÃO",
        4: "Jose PUTAO",
        5: "Nicolas FODAO"
    }
    
    return lista.get(opcao, "Opção inválida")

def menu():
    while True:
        print("\nMenu de Melhores lista")
        print("1. Andrey")
        print("2. Otavio")
        print("3. Lucas")
        print("4. Jose")
        print("5. Nicolas")
        print("0. Sair")
        
        try:
            escolha = int(input("Digite o número do amigo (ou 0 para sair): "))
            
            if escolha == 0:
                print("Saindo...")
                break
            
            mensagem = mostrar_lista(escolha)
            print(f"Você escolheu: {mensagem}")
        
        except ValueError:
            print("Por favor, digite um número válido.")

menu()
