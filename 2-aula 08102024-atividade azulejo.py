# Entrada de dados onde input é entrada de dados e float números reais#
comprimento = float(input("Digite o comprimento da cozinha (em metros): "))
largura = float(input("Digite a largura da cozinha (em metros): "))
altura = float(input("Digite a altura da cozinha (em metros): "))

# Cálculo da área das paredes
area_paredes = 2 * altura * (comprimento + largura)

# Cada caixa de azulejos possui 1,5 m²
area_por_caixa = 1.5

# Cálculo da quantidade de caixas necessárias
quantidade_caixas = area_paredes / area_por_caixa

# Arredondar para cima usando int
quantidade_caixas = int(quantidade_caixas) + 1 if quantidade_caixas % 1 != 0 else int(quantidade_caixas)

# Saída
print(f"Quantidade de caixas de azulejos necessárias: {quantidade_caixas}")


