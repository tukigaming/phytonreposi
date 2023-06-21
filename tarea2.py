def es_primo(numero):
    if numero < 2:
        return False
    return all(numero % i != 0 for i in range(2, int(numero**0.5) + 1))

numero = int(input("Ingresa un número: "))
if es_primo(numero):
    print("Es primo")
else:
    multiplos = [i for i in range(1, numero + 1) if numero % i == 0]
    print("No es primo")
    print("Multiplos:", multiplos)