def main():
    while True:
        print("\n=== MENÚ CALCULADORA ===")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 5:
                print("¡Gracias por usar la calculadora!")
                break

            if opcion < 1 or opcion > 5:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
                continue

            if opcion == 1:
                print("=== SUMA ===")
                try:
                    num1 = float(input("Ingrese el primer número: "))
                    num2 = float(input("Ingrese el segundo número: "))
                    resultado = num1 + num2
                    print(f"El resultado de la suma es: {resultado}")
                except ValueError:
                    print("Error: Por favor ingrese números válidos")

            elif opcion == 2:
                print("=== RESTA ===")
                try:
                    num1 = float(input("Ingrese el primer número: "))
                    num2 = float(input("Ingrese el segundo número: "))
                    resultado = num1 - num2
                    print(f"Resultado: {num1} - {num2} = {resultado}")
                except ValueError:
                    print("Error: Debes ingresar números válidos.")

            elif opcion == 3:
                print("=== MULTIPLICACIÓN ===")
                try:
                    num1 = float(input("Ingrese el primer número: "))
                    num2 = float(input("Ingrese el segundo número: "))
                    resultado = num1 * num2
                    print(f"Resultado de la multiplicación: {resultado}")
                except ValueError:
                    print("Error: Por favor ingrese números válidos")

            elif opcion == 4:
                print("TODO: Implementar división")
                # TODO: Agregar funcionalidad de división

        except ValueError:
            print("Error: Por favor, ingrese un número válido")

if __name__ == "__main__":
    main()
