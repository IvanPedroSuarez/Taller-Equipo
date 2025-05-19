class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: No se puede dividir por cero"

def main():
    calculadora = Calculadora()

    while True:
        print("\n=== CALCULADORA ===")
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

            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == 1:
                resultado = calculadora.suma(num1, num2)
                print(f"Resultado: {resultado}")
            elif opcion == 2:
                resultado = calculadora.resta(num1, num2)
                print(f"Resultado: {resultado}")
            elif opcion == 3:
                resultado = calculadora.multiplicacion(num1, num2)
                print(f"Resultado: {resultado}")
            elif opcion == 4:
                resultado = calculadora.division(num1, num2)
                print(f"Resultado: {resultado}")

        except ValueError:
            print("Error: Por favor, ingrese números válidos")

if __name__ == "__main__":
    main()
