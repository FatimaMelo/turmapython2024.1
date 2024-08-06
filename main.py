def criar_cardapio():

    print("Food Truck - Matador de Fome!")
    print("Cardápio:")
    print("1. Hambúrguer - R$ 7,00")
    print("2. Refrigerante- R$ 5,00")
    print("3. Cachorro Quente - R$ 6,00")
    print("4. Guaracamp - R$ 3,00")
    print("5. Fechar a conta")


def calcular_conta(itens):

    total = 0
    for item in itens:
        if item == 1:
            total += 7.00
        elif item == 2:
            total += 5.00
        elif item == 3:
            total += 6.00
        elif item == 4:
            total += 3.00
    return total



pedidos = []

resp = 'S'
while resp == 'S':
    criar_cardapio()
    escolha = int(input("Digite o número do item que você deseja (ou 5 para fechar a conta): "))

    if escolha == 5:
        break
    pedidos.append(escolha)



total_conta = calcular_conta(pedidos)
print(f"O valor total da sua conta é R$ {total_conta:.2f}")
