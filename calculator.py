#// Crea un calulador de operaciones matemáticas básicas
#// que permita sumar, restar, multiplicar y dividir dos números
#// y que imprima el resultado en la consola.
#// El programa debe pedir al usuario que ingrese dos números y la operación a realizar
#// y luego mostrar el resultado en la consola.
#// El programa debe manejar errores como la división por cero y la entrada de datos no válidos.
#// El programa debe estar estructurado en funciones y utilizar comentarios para explicar el código.
#// El programa debe estar escrito en Python y debe ser fácil de entender y mantener.
def add(x, y):
    """Suma dos números."""
    return x + y
def subtract(x, y):
    """Resta dos números."""
    return x - y
def multiply(x, y):
    """Multiplica dos números."""
    return x * y
def divide(x, y):
    """Divide dos números. Maneja la división por cero."""
    if y == 0:
        return "Error: División por cero no permitida."
    return x / y
def calculator():
    """Calculadora de operaciones matemáticas básicas."""
    print("Bienvenido a la calculadora.")
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    while True:
        try:
            choice = input("Ingrese su elección (1/2/3/4): ")
            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                
                next_calculation = input("¿Desea realizar otra operación? (si/no): ")
                if next_calculation.lower() != 'si':
                    break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor ingrese números.")
if __name__ == "__main__":
    calculator()
# Este programa es una calculadora simple que permite realizar operaciones matemáticas básicas
# como suma, resta, multiplicación y división.
# Maneja errores como la división por cero y entradas no válidas.
# El código está estructurado en funciones para facilitar su comprensión y mantenimiento.
# El programa solicita al usuario que ingrese dos números y la operación a realizar,
# y luego muestra el resultado en la consola.
# El programa permite realizar múltiples cálculos hasta que el usuario decida salir.
# El código está escrito en Python y utiliza comentarios para explicar su funcionamiento.
# El programa es fácil de entender y mantener, lo que lo hace adecuado para principiantes en programación.
# El programa utiliza un bucle while para permitir al usuario realizar múltiples cálculos
# y maneja excepciones para evitar errores de entrada.
# El programa es interactivo y fácil de usar, lo que lo hace adecuado para cualquier persona
# que necesite realizar cálculos matemáticos básicos.
# El programa es una herramienta útil para estudiantes, profesionales y cualquier persona
# que necesite realizar cálculos matemáticos simples.
# El programa es fácil de entender y mantener, lo que lo hace adecuado para principiantes en programación.
# El programa es una calculadora simple que permite realizar operaciones matemáticas básicas
# como suma, resta, multiplicación y división.
# Maneja errores como la división por cero y entradas no válidas.
# El código está estructurado en funciones para facilitar su comprensión y mantenimiento.