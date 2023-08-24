""" Reescribe el programa del salario usando try y except, de modo que el
programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
un mensaje y saliendo del programa. """

def calcular_salario():
    
    # El try convierte las entradas del usuario en valores numericos
    try:
        salario_bruto = float(input("Ingresar el salario bruto : "))
        total_horas_trabajadas = float(input("Ingresar el total de horas trabajadas: "))
        
        salario_total = salario_bruto * total_horas_trabajadas
        print("El salario bruto total es:", salario_total)
        
        # El except captura las excepciones especificas 
        # ValueError (mostrara el mensaje de error)
    except ValueError:
        print("Error: por favor introducir un numero.")
        
        # KeyboardInterrupt (manejara la interrupcion del usuario)
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")

if __name__ == "__main__":
    calcular_salario()
