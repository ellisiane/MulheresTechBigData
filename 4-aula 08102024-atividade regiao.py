# Tabela de região
tabela_procedencia = {
    '1': 'Norte',
    '2': 'Nordeste',
    '3': 'Centro-Oeste',
    '4': 'Sudeste',  
    '5': 'Sul',

}

# Código de origem do produto (input interação com usuário)
codigo_origem = input("Digite o código de origem do produto: ")

# Verificação da procedência (If = se  in= dentro)
if codigo_origem in tabela_procedencia:
    regiao_procedencia = tabela_procedencia[codigo_origem]
    print("Região de procedência:", regiao_procedencia)
else:
    print ("Região de procedência desconhecida")