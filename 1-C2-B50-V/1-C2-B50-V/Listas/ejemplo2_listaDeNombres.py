nombres=['Diego','Camila','Esteban','Alexis','Alfredo']

#mostrando TODA la lista de nombres
# print(nombres)

# mostrando UN elemento de la lista, en este caso a Camila
# Observa que 'Camila' está en la posición 1 de la lista
# print(nombres[5])

# RECORRIENDO UNA LISTA - Forma 1: Usando for-range
print("\nRecorriendo la lista usando for-range")
largo=len(nombres)
for i in range(largo):
    print("En la posición",i,"está:",nombres[i])

# RECORRIENDO UNA LISTA - Forma 2: Usando for-iterable
print("\nRecorriendo la lista usando iterable")
for item in nombres:
    print(item)


