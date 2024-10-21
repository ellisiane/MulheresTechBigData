#ACESSO À DATASETS EXTERNOS:

#https://www.kaggle.com/datasets/mohammedadham45/udemy-courses?select=UdemyCoursesDataset.csv
import pandas as pd
cs_udemy = pd.read_csv('UdemyCoursesDataset.csv')
print(cs_udemy.head())  # Exibe as cinco primeiras linhas
print(cs_udemy.tail()) # Exibe as cinco última linhas

# #Leitura de Arquivos e Filtragem:


print(cs_udemy.to_string()) #Exibe o DataFrame completo como uma string, útil para visualização.

pd.set_option('display.max_rows', 3)


# # Filtragem de Dados: #Exemplo de filtragem por colunas e linhas específicas:

df_filtrado = cs_udemy[(cs_udemy['course_id'] == 288942) & (cs_udemy['course_title'] == '#1 Piano Hand Coordination: Play 10th Ballad in Eb Key songs')]
print(df_filtrado)


288942,#1 Piano Hand Coordination: Play 10th Ballad in Eb Key songs


# #Atividade Prática:
# #
# #Através do Kaggle, procurem outros datasets e apliquem os comandos trabalhados anteriormente.