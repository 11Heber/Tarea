"""Escribe un programa para pedirle al usuario el número de
horas y la tarifa por hora para calcular el salario bruto."""

# Solicitar al usuario el número de horas y la tarifa por hora
horas_normales_trabajadas = float(input("Ingresar el número de horas normales trabajadas: "))
# Solicitar al usuario el costo de hora trabajada
tarifa_por_hora_normal = float(input("Ingresar la tarifa por hora normal: "))

horas_dobles_trabajadas = float(input("Ingresar el número de horas dobles trabajadas: "))
tarifa_por_hora_doble = float(input("Ingresar la tarifa por hora doble: "))

horas_extras_trabajadas = float(input("Ingresar el número de horas extras trabajadas: "))
tarifa_por_hora_extra = float(input("Ingresar la tarifa por hora extra: "))

total_impuestos_a_reducir = float(input("Ingresar la cantidad de Impuestos: "))

# Calcular el salario bruto
salario_bruto_horas_normales = horas_normales_trabajadas * tarifa_por_hora_normal
salario_bruto_horas_dobles = horas_dobles_trabajadas * tarifa_por_hora_doble
salario_bruto_horas_extras = horas_extras_trabajadas * tarifa_por_hora_extra

# Mostrar el resultado del salario bruto
print("El salario bruto a devengar es:", salario_bruto_horas_normales + salario_bruto_horas_dobles + salario_bruto_horas_extras - total_impuestos_a_reducir )
