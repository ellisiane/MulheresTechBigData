# 3) Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um 
# programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de combustível gasto e o 
# valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia;

# Entrada de dados
inicio_dia = float(input("Digite a marcação do odômetro no início do dia (km): "))
fim_dia = float(input("Digite a marcação do odômetro no final do dia (km): "))
litros_gastos = float(input("Digite o número de litros de combustível gasto: "))
valor_recebido = float(input("Digite o valor total recebido dos passageiros (R$): "))
preco_combustivel = 4.87  # Preço fixo do combustível

# Usando while para calcular a média de consumo
km_rodados = fim_dia - inicio_dia
i = 0
media_consumo = 0
while i < 1:
    media_consumo = km_rodados / litros_gastos
    i += 1

# Usando for com range para calcular o lucro líquido
custo_combustivel = 0
for _ in range(int(litros_gastos)):
    custo_combustivel += preco_combustivel

lucro_liquido = valor_recebido - (custo_combustivel / litros_gastos * litros_gastos)

# Exibir os resultados
print(f"Média de consumo: {media_consumo:.2f} km/L")
print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")