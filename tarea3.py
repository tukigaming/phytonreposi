def factorial(numero):
    if numero < 0:
        return None
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Ingresa un número: "))
resultado = factorial(numero)
if resultado is None:
    print("No se puede calcular el factorial de un número negativo")
else:
    print("El factorial de", numero, "es", resultado)