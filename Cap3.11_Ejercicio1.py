""" Reescribe el programa del cálculo del salario para darle al empleado
1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.
 """

# Calculo del salario por 1.5 veces
def calcular_salario(tarifa_horaria, total_horas_trabajadas):
    if total_horas_trabajadas <= 40:
        salario = tarifa_horaria * total_horas_trabajadas
    else:
        horas_normales = 40
        horas_extra = total_horas_trabajadas - horas_normales
        salario = (tarifa_horaria * horas_normales) + (1.5 * tarifa_horaria * horas_extra)
    return salario


# Pedir al usuario la tarifa horaria y las horas trabajadas
total_horas_trabajadas = float(input("Ingresar el total de horas trabajadas: "))
tarifa_horaria = float(input("Ingresar la tarifa horaria: "))

# Calcular y mostrar el salario
salario_total = calcular_salario(tarifa_horaria, total_horas_trabajadas)
print("El salario bruto a devengar es:", salario_total)
