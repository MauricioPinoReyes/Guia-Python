horasTrab=int(input("Cantidad de horas trabajadas: "))
if horasTrab > 40:
    hrsExtras=horasTrab-40
    sueldoSemanal=hrsExtras*7500 + 40*5000
else:
    sueldoSemanal=horasTrab*5000
print("Tu sueldo semanal es:",sueldoSemanal)
