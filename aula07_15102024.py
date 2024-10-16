# lista1=[2,4,6,8,10]
# lista1.remove(6) #removeu  elemento 6 pelo próprio elemento
# lista1.remove(lista1[2]) #removeu  elemento de índice 
# print(lista1) #[2,4,9]

# lista2=lista1.insert(2,1000)
# print(lista2) # vai resultar em "none"
# lista2=lista1.copy()
# print(lista2) #[2,4,1000,10]

# lista3=lista1.copy()
# lista4=lista1.copy()
# lista3.clear() #limpa todo conteúdo da linha deixando vazia
# print(lista3) #[]
# lista4.pop(0) #
# print(lista4) #[4,1000,10]
# lista4.sort() # coloquei meus elementos da lista em ordem crescente
# print(lista4) #[4,10,1000]
# lista4.reverse()
# print(lista4) #[1000,10,4]

# #print(lista1,lista2,lista3,lista4)

frutas=["uva","maça","carambola","melancia"]
frutas.sort() #o comando também funciona para elementos do tipo string
print(frutas)

#TUPLAS #SÃO IMUTÁVEIS: podemos consultar
frutas2=tuple(frutas)
print(frutas2.index("uva")) # eu consultei em qual índice se encontra o elemento uva
print(frutas2.count("uva"))


#DICIONÁROS: estruturas que salvam as informações

estados={'RJ': 'Rio de Janeiro',
         'SP': 'SÃO PAULO',
        'MG':'Minas Gerais',
        'ES': 'Espírito Santo'}

print(estados)

print(estados.keys())
print(estados.values()) # Valores

candidatos={ 'Larissa':28,
             'Anna':20
        
  }
