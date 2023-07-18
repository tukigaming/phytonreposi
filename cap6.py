
#Las modificaciones necesarias para el antiguo Python 2 se encuentran en los comentarios.

# Devuelve el índice de x en arr si está presente, de lo contrario -1
def binary_search(arr, low, high, x):

	# Compruebe el caso base
	if high >= low:

		mid = (high + low) // 2

		# Si el elemento está presente en el medio mismo
		if arr[mid] == x:
			return mid

		# Si el elemento es más pequeño que el medio, entonces solo puede
		# estar presente en el subarreglo izquierdo
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# De lo contrario, el elemento solo puede estar presente en el subarreglo derecho
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# El elemento no está presente en la matriz
		return -1

# Matriz de prueba
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Llamada de función
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("existe el numero", str(result))
else:
	print("el numero no existe en la matriz")
