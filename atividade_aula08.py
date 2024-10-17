
# #ATIVIDADES:

# #1) Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.

# peso = float(input("Insira o peso: "))

# def calculo_multa():
#     if peso > 100:
#         multa = (peso / 3) + 5.0
#         print(f'Peso permitido ultrapassado,pague: R$ {multa:.2f}')
#     else:
#        return print("Não precisa pagar multa")

# calculo_multa()

# 2) Crie um programa que faça a leitura da altura e do peso de N pessoas para o cálculo do IMC, mostrando ao final a classificação de acordo
# com a tabela de IMC.

# def calcular_imc(peso, altura):
#     return peso / (altura ** 2) # peso / altura elevado ao quadrado

# n = int(input("Número de pessoas: ")) #entrada do usúario com o número de pessoas que aparecera como número inteiro por causa do int

# for _ in range(n):  #loop executado n vezes
#     peso = float(input("Peso (kg): ")) 
#     altura = float(input("Altura (m): "))
#     imc = calcular_imc(peso, altura)
#     if imc < 18.5:    ### aqui inicia uso das condicionais
#         classificacao = "Abaixo do peso"
#     elif 18.5 <= imc < 24.9:
#         classificacao = "Peso normal"
#     elif 25 <= imc < 29.9:
#         classificacao = "Sobrepeso"
#     elif 30 <= imc < 34.9:
#         classificacao = "Obesidade Grau I"
#     elif 35 <= imc < 39.9:
#         classificacao = "Obesidade Grau II"
#     else:
#         classificacao = "Obesidade Grau III"  ###### aqui termina o uso das condicionais
    
#     print(f"IMC: {imc:.2f} - {classificacao}") # mostra imc com duas casas decimais

# 3) Crie funções que mostrem um cardápio de um restaurante (pelo menos 4 itens) e que permitam realizar pedidos e fechar a conta.

# def mostrar_cardapio():
#     print("1. Couvert - R$ 15.00\n2. Prato principal - R$ 40.00\n3. Sobremesa - R$ 20.00\n4. Bebida - R$ 10.00")

# def realizar_pedido():
#     pedidos = {}
#     while True:
#         item = int(input("Escolha um item (1-4) ou 0 para fechar: "))
#         if item == 0:
#             break
#         if item in [1, 2, 3, 4]:
#             quantidade = int(input("Quantidade: "))
#             if item in pedidos:
#                 pedidos[item] += quantidade
#             else:
#                 pedidos[item] = quantidade
#         else:
#             print("Opção inválida.")
#     return pedidos

# def fechar_conta(pedidos):
#     precos = {1: 15.00, 2: 40.00, 3: 20.00, 4: 10.00}
#     total = sum(precos[item] * quantidade for item, quantidade in pedidos.items())
#     print(f"Total: R$ {total:.2f}")

# # Executar as funções na sequência
# mostrar_cardapio()
# pedidos = realizar_pedido()
# fechar_conta(pedidos)