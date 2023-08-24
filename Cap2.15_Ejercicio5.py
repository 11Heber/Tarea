""" Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a 
grados Fahrenheit e imprima por pantalla la temperatura convertida """


# Solicitar al usuario la temperatura en grados Celsius
celsius = float(input("Ingresar una temperatura en grados Celsius: "))


# Conversion de temperatura Celsius a temp. Fahrenheit 
# fórmula de Fahrenheit: F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32


# Impresion en pantalla de la temperatura ya convertida en grados Fahrenheit
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

