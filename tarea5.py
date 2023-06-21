def Fibonacci(n):
    print(f"Calculando Fibonacci({n})")
    if n < 2:
        return n
    else:
        print(f"Recursión: Fibonacci({n-1}) + Fibonacci({n-2})")
        return Fibonacci(n-1) + Fibonacci(n-2)

print("Calculando Fibonacci(5)")
resultado_5 = Fibonacci(5)
print(f"Resultado: {resultado_5}\n")

print("Calculando Fibonacci(4)")
resultado_4 = Fibonacci(4)
print(f"Resultado: {resultado_4}\n")

print("Calculando Fibonacci(3)")
resultado_3 = Fibonacci(3)
print(f"Resultado: {resultado_3}\n")

print("Calculando Fibonacci(2)")
resultado_2 = Fibonacci(2)
print(f"Resultado: {resultado_2}\n")

print("Calculando Fibonacci(1)")
resultado_1 = Fibonacci(1)
print(f"Resultado: {resultado_1}\n")

