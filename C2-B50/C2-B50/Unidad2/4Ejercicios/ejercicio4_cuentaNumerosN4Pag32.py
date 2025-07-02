n=int(input("Cuántos números vas a ingresar (n): "))
cn=cp=cneg=0
for i in range(n):
    num=int(input("Ingresa un número: "))
    if num == 0:
        cn += 1
    elif num > 0:
        cp += 1
    else:
        cneg += 1
print("Cantidad de número positivos :",cp)
print("Cantidad de número negativos :",cneg)
print("Cantidad de número neutro    :",cn)

