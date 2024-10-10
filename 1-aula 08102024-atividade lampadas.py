# 1) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
# Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que 
# a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada;

# Dados de entrada
potencia_lampada = float(input("Digite a potência da lâmpada (em watts): "))
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

# Cálculos
area_comodo = largura * comprimento
potencia_necessaria = area_comodo * 3
num_lampadas = potencia_necessaria / potencia_lampada
num_bocais = area_comodo / 3
num_lampadas_necessarias = num_lampadas if num_lampadas > num_bocais else num_bocais

# Saída
print(f"Número de lâmpadas necessárias: {int(num_lampadas_necessarias)}")
