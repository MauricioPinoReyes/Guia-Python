from persona import Persona
lista=[]
p=Persona(1,"Angel",25)
lista.append(p)
p=Persona(2,"Camila",24)
lista.append(p)
p=Persona(3,"Alexis",28)
lista.append(p)

# 1:Recorriendo la lista usando range (posicion)
print("\nMostrando la lista usando range")
for i in range(len(lista)):
    print(lista[i].mostrarPersona())

# 1:Recorriendo la lista usando iterable
print("\nMostrando la lista usando iterable")
for item in lista:
    print(item.mostrarPersona())
    