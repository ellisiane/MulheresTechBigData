# Dados de entrada
potencia_lampada = float(input("Digite a potência da lâmpada (em watts): "))
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

# Cálculos
area_comodo = largura * comprimento
potencia_necessaria = area_comodo * 3
num_lampadas = potencia_necessaria / potencia_lampada
num_bocais = area_comodo / 3

# Decisão usando if-else
if num_lampadas > num_bocais:
    num_lampadas_necessarias = num_lampadas
else:
    num_lampadas_necessarias = num_bocais

# Saída
print(f"Número de lâmpadas necessárias: {int(num_lampadas_necessarias)}")
