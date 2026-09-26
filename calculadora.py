def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def mostrar_menu():
    print("\n" + "*" * 30)
    print("   CALCULADORA EN PYTHON")
    print("=" * 30)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("=" * 30)

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "5":
            print("\nSaliendo de la calculadora. ¡Hasta luego!")
            break

        if opcion in ["1", "2", "3", "4"]:
            try:
                num1= float(input("Ingrese el primer número: "))
                num2= float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos.")
                continue
            if opcion == "1":
                print(f"\nResultado de la suma: {num1} + {num2} = {suma(num1, num2)}")
            elif opcion == "2":
                print(f"Resultado de la resta: {num1} - {num2} = {resta(num1, num2)}")
            elif opcion == "3":
                print(f"Resultado de la multiplicación: {num1} * {num2} = {multiplicacion(num1, num2)}")
            elif opcion == "4":
                print(f"Resultado de la división: {num1} / {num2} = {division(num1, num2)}")
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")