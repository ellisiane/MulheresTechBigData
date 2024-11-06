# 5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
# nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
# está em exame, de acordo com as informações abaixo: 
# Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;


nota1=float(input("Primeira Nota:"))
nota2=float(input("Segunda Nota:"))
nota_opt=float(input("Nota optativa:"))

if nota_opt !=-1:
    menor_nota=min(nota1,nota2)
    if nota_opt>menor_nota:
        if nota1==menor_nota:
           nota1=nota_opt 
    else:    
        nota1=nota_opt

media=(nota1+nota2)/2       
print(f'Média:{media}')     

if media>=6.0:
    print("Aprovado")
elif media <3.0:
    print("Reprovado")
else:
    print("Exame de Recuperação")

          
