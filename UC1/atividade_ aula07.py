# # Crie um código que seja capaz de ler e armazenar
# # uma sequência de 20 números pares e 20 números ímpares
# # Obs: Utilize estruturas de repetição para fechar esse cojunto de
# # números 

# # Inicializar listas para armazenar os números pares e ímpares
# pares = []
# impares = []

# # Ler e armazenar 20 números pares fornecidos pelo usuário
# print("Digite 20 números pares:")
# while len(pares) < 20:
#     numero = int(input(f"Número par {len(pares) + 1}: "))
#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         print("Esse número não é par. Tente novamente.")

# # Ler e armazenar 20 números ímpares fornecidos pelo usuário
# print("Digite 20 números ímpares:")
# while len(impares) < 20:
#     numero = int(input(f"Número ímpar {len(impares) + 1}: "))
#     if numero % 2 != 0:
#         impares.append(numero)
#     else:
#         print("Esse número não é ímpar. Tente novamente.")

# # Exibir os números pares e ímpares armazenados
# print("Números Pares:", pares)
# print("Números Ímpares:", impares)