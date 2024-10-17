# #FUNÇÕES:

# def somar(parametro1,parametro2): #nesse exemplo: como eu disse quem são meus argumentos, eu preciso...
#     return parametro1+parametro2
# print(somar(20,30)) #...ter a informação deles pro meu print.

# def subtrair(): #nesse exemplo, eu não disse quem são os argumentos da função, pois já tenho inputs dentro dela. Com isso...
#     parametro1=int(input('Número 1:'))
#     parametro2=int(input('Número 2:'))
#     return parametro1-parametro2

# print(subtrair()) #...eu consigo executar a função sem precisar fornecer alguma informação no print.

# #EXEMPLO DE APRIMORAMENTO: (aula dia 08-out)

# # 5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
# # nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
# # está em exame, de acordo com as informações abaixo: 
# # Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;

# def boletim():
#     nota1=float(input('Primeira Nota:'))
#     nota2=float(input('Segunda Nota:'))
#     nota_opt=float(input('Nota Optativa:'))

#     if nota_opt != -1: 
#         menor_nota=min(nota1,nota2)
#         if nota_opt>menor_nota:
#             if nota1==menor_nota:
#                 nota1=nota_opt
#             else:
#                 nota2=nota_opt

#     media=(nota1+nota2)/2
#     print(f'Média:{media}')

#     if media >= 6.0:
#         print("Aprovado")
#     elif media < 3.0:  

#         print("Reprovado")
#     else:
#         print("Exame de Recuperação")

# boletim()

#ATIVIDADE ASSISTIDA:

#Crie uma função para multiplicar dois números quaisquer:

# def multiplicar(num1=1,num2=2):
#     num1=float(input('Digite o primeiro número:'))
#     num2=float(input('Digite o segundo número:'))
#     return f'O resultado dos dois números multiplicados é {num1*num2}.'

# print(multiplicar())

# 3) Crie funções que mostrem um cardápio de um restaurante (pelo menos 4 itens) e que permitam realizar pedidos e fechar a conta.

def mostrar_cardapio():
    print("1. Couvert - R$ 15.00\n2. Prato principal - R$ 40.00\n3. Sobremesa - R$ 20.00\n4. Bebida - R$ 10.00")

def realizar_pedido():
    pedidos = []
    while True:
        item = int(input("Escolha um item (1-4) ou 0 para fechar: "))
        if item == 0:
            break
        pedidos.append(item)
    return pedidos

def fechar_conta(pedidos):
    precos = {1: 15.00, 2: 40.00, 3: 20.00, 4: 10.00}
    total = sum(precos[i] for i in pedidos)
    print(f"Total: R$ {total:.2f}")

mostrar_cardapio()
pedidos = realizar_pedido()
fechar_conta(pedidos)