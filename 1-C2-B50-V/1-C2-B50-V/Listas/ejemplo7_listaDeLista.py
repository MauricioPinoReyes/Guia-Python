datos = [['Alfredo',35,4.8,True],
         ['Jocelyn',28,5.2,True],
         ['Francisco',30,6.1,False],
         ['Alexis',31,5.7,True],
         ['Ximena',32,4.3,False]]

#print("\nRecorriendo la lista usando iterable")
#for item in datos:
#    print(item)

"""
print("\nRecorriendo la lista usando doble ciclo for-range")
for i in range(len(datos)):
    for j in range(4):
        print(datos[i][j])
"""
for i in range(len(datos)):
    print("\nDatos de : ",datos[i][0])
    print("- Edad   : ",datos[i][1])
    print("- Nota   : ",datos[i][2])
    if datos[i][3]:
        print("- Estado : ACTIVO")
    else:
        print("- Estado : INACTIVO")





