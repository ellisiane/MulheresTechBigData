###AULA10 - 18/10/2024###
#
# Pandas
#
import pandas as pd #(pd=alias)
print(pd.__version__)

#CRIAÇÃO DE UM DATASET:

data = {'Cargo': ['Analista', 'Gerente', 'Estagiário'],
        'Salário': [4500, 9000, 2000]}
df = pd.DataFrame(data)
print(df)

#CRIAÇÃO DE UMA SÉRIE:'

cargos = pd.Series(['Analista', 'Gerente', 'Estagiário'], index=[1, 2, 3])
print(cargos)

#ATIVIDADE ASSISTIDA:

#Crie um dataset de 3 colunas com as seguintes informações: 'nome de um filme', 'ano de lançamento' e 'gênero'.
import pandas as pd

data_cinema={'Título':['Cidade de Deus','Divertidamente 2','Uma Linda Mulher'],
        'Ano de Lançamento':[2002,2024,1990],
         'Gênero':['Drama','Animação','Romance']   
        }

data_cinema=pd.DataFrame(data_cinema)
print (data_cinema)

#ACESSO À DATASETS EXTERNOS:

#https://www.kaggle.com/datasets/thebumpkin/700-classic-disco-tracks-with-spotify-data
import pandas as pd
df_disco = pd.read_csv('Classicdisco.csv')
print(df_disco.head())  # Exibe as cinco primeiras linhas
print(df_disco.tail()) # Exibe as cinco última linhas

#Leitura de Arquivos e Filtragem:


print(df_disco.to_string()) #Exibe o DataFrame completo como uma string, útil para visualização.

print(df_disco.max_rows()) #Define o número máximo de linhas a ser exibido.

# Filtragem de Dados: #Exemplo de filtragem por colunas e linhas específicas:

# df_filtrado = df_disco[df_disco['Artista'] == 'Bee Gees']
# print(df_filtrado)

# #Criação de Novas Colunas: adicionar colunas derivadas

# df_disco['Duração_Minutos'] = df_disco['Duração_Segundos'] / 60

#Leitura de Arquivos Excel e Outros Formatos:
df_disco_2 = pd.read_excel('seuarquivo.xlsx')
df_disco_3 = pd.read_json('seuarquivo.json')
df_disco_4 = pd.read_hdf('seuarquivo.html')
df_disco_5 = pd.read_sql('seuarquivo.sql')

#Atividade Prática:
#
#Através do Kaggle, procurem outros datasets e apliquem os comandos trabalhados anteriormente.


