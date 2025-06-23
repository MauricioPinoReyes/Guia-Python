n=int(input("Cuántos números vas a ingresar (n): "))
for i in range(n):
    num=int(input("Ingresa un número: "))
    #cubo=num*num*num
    cubo=num**3
    #cuarta=num*cubo
    cuarta=num**4
    print(num,"elevado a 3 es:",cubo)
    print(num,"elevado a 4 es:",cuarta)

