
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b


def calculadora():
    print("Calculadora en Python")
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Selecciona una opción (1/2/3/4): ")

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida")
        return

    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Por favor, introduce números válidos.")
        return

    if opcion == "1":
        resultado = sumar(num1, num2)
    elif opcion == "2":
        resultado = restar(num1, num2)
    elif opcion == "3":
        resultado = multiplicar(num1, num2)
    elif opcion == "4":
        resultado = dividir(num1, num2)

    print("Resultado:", resultado)


if __name__ == "__main__":
    calculadora()
