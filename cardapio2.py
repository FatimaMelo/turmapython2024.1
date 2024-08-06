# função para criar o cardapio


def criar_cardapio():
    cardapio = {
        "1": {"item": "pizza", "preco": 50.00},
        "2": {"item": "hot dog", "preco": 12.00},
        "3": {"item": "empada", "preco": 5.00},
        "4": {"item": "churrasco misto", "preco": 20.00},
        "5": {"item": "ratatouille", "preco": 70.00},
        "6": {"item": "fechar conta", "preco": 0.00}
    }
    return cardapio


def calcular_conta():
    cardapio = criar_cardapio()
    total = 0.0

    while True:
        print("Cardápio:")
        for codigo, item in cardapio.items():
            print(f"{codigo}: {item['item']} - R${item['preco']:.2f}")

        opcao = input("Digite o código do item que deseja (ou '6' para fechar a conta): ")

        if opcao == "6":
            print(f"Total da conta: R${total:.2f}")
            break

        if opcao in cardapio:
            total += cardapio[opcao]["preco"]
            print(f"Você adicionou {cardapio[opcao]['item']} à sua conta.")
        else:
            print("Opção inválida. Tente novamente.")



calcular_conta()