import math

historial= []

def guardar_historial(operacion_str, resultado):
    registro = f"{operacion_str} = {resultado}"
    historial.append(registro)

def sumar_varios(numeros):
    return sum(numeros)

def restar_varios(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado

def multiplicar_varios(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def dividir_varios(a,b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

# -----------Operaciones avanzadas estadisticas-----------

def potencia(base, exponente):
    return math.pow(base, exponente)

def raiz_cuadrada(numero):
    if numero < 0:
        return "Error: No se puede calcular la raiz cuadrada de un numero negativo."
    return math.sqrt(numero)

def porcentaje(valor, porcentaje):
    return (valor * porcentaje) / 100

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

#-----------Funciones auxiliares de entrada de datos-----------

def pedir_lista_numeros():
    while True:
        entrada= input("Ingrese los numeros separados por comas (ejemplo: 1,2,3,4): ")
        try:
            numeros= [float(n.strip()) for n in entrada.split(",") if n.strip() != '']
            if not numeros:
                print("No se ingresaron nmeros válidos. Intente nuevamente.")
                continue
            return numeros
        except ValueError:
            print("Entrada invalida. Asegurese de ingresar solo numeros separados por comas.")

def pedir_un_numero(mensaje="Ingresa un numero: "):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingrese un valor numerico valido.")

#-----------MENU-----------

def mostrar_menu():
    print("\n" + "=" * 30)
    print("     Calculadora PYTHON")
    print("=" * 40)
    print("1. Sumar varios numeros")
    print("2. Restar varios numeros")
    print("3. Multiplicar varios numeros")
    print("4. Dividir dos numeros")
    print("5. Potencia (base ^ exponente)")
    print("6. Raiz cuadrada")
    print("7. Porcentaje (% de X)")
    print("8. Estadisticas (Promedio, Max, Min)")
    print("9. Mostrar historial de operaciones")
    print("0. Salir")
    print("=" * 40)

def mostrar_historial():
    print("\n----HISTORIAL DE OPERACIONES----")
    if not historial:
        print("Aun no se han realizado operaciones.")
    else:
        for idx, item in enumerate(historial, 1):
            print(f"{idx}. {item}")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion= input("Seleccione una opcion (0-9): ").strip()

        if opcion == "0":
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        elif opcion in ["1", "2", "3"]:
            nums= pedir_lista_numeros()
            if opcion == "1":
                res= sumar_varios(nums)
                expr = "+".join(str(n) for n in nums)
            elif opcion == "2":
                res= restar_varios(nums)
                expr = "-".join(str(n) for n in nums)
            elif opcion == "3":
                res= multiplicar_varios(nums)
                expr = "*".join(str(n) for n in nums)

            print(f"\nResultado: {expr} = {res}")
            guardar_historial(expr, res)

        elif opcion == "4":
            a= pedir_un_numero("Ingrese el primer numero: ")
            b= pedir_un_numero("Ingrese el segundo numero: ")
            res= dividir_varios(a, b)
            print(f"\nResultado: {a} / {b} = {res}")
            guardar_historial(f"{a}/{b}", res)

        elif opcion == "5":
            base= pedir_un_numero("ingrese la base: ")
            exponente= pedir_un_numero("Ingrese el exponente: ")
            res= potencia(base, exponente)
            print(f"\nResultado: {base}^{exponente} = {res}")
            guardar_historial(f"{base}^{exponente}", res)

        elif opcion == "6":
            num= pedir_un_numero("Ingrese el numero: ")
            res= raiz_cuadrada(num)
            print(f"\nResultado: sqrt({num}) = {res}")
            guardar_historial(f"sqrt({num})", res)

        elif opcion == "7":
            base_num = pedir_un_numero("Ingrese la cantidad total: ")
            porc = pedir_un_numero("Ingrese el porcentaje a calcular (%): ")
            res = porcentaje(base_num, porc)
            print(f"\nResultado: {porc}% de {base_num} = {res}")
            guardar_historial(f"{porc}% de {base_num}", res)

        elif opcion == "8":
            nums = pedir_lista_numeros()
            prom= calcular_promedio(nums)
            maximo= max(nums)
            minimo= min(nums)
            print(f"\n--- Resultados Estadisticos ---")
            print(f"Cantidad de elementos: {len(nums)}")
            print(f"Promedio: {prom}")
            print(f"Maximo: {maximo}")
            print(f"Minimo: {minimo}")
            guardar_historial(f"Estadisticas de {nums}", f"Promedio: {prom}, Max: {maximo}, Min: {minimo}")

        elif opcion == "9":
            mostrar_historial()

        else:
            print("Opcion invalida. Por favor, seleccione una opcion del 0 al 9.")