def identity(x):
    return x  # Función identidad

import SortArray

class Array(SortArray.Array):
    # Clase Array nueva basada en SortArray

    def partition_rec(self, pivot, lo=0, 
                      hi=None, key=identity):
        # Particiona recursivamente el arreglo en movimiento
        # elementos cuyas claves son inferiores o iguales
        # a un valor de pivote a la izquierda/baja
        # y el resto a la derecha/alta

        if hi is None:
            hi = len(self) - 1  

        while lo <= hi and key(self.get(lo)) < pivot:
            lo += 1
        while lo < hi and pivot < key(self.get(hi)):
            hi -= 1
        if lo >= hi:    
            return lo    
        self.swap(lo, hi)    
        return self.partition_rec(pivot, lo + 1, hi - 1, key)
        # Incrementar lo hasta que supere a hi
            # o encontremos una clave que no esté en la partición inferior
            

        
            # Decrementar hi hasta que coincida con lo
            # o encontremos el pivote o una clave que no esté en la partición superior
            

        
            # Si lo está en o por encima de hi, entonces
            # la partición inferior termina en lo
            

        
        # De lo contrario, intercambiar los elementos en lo y hi

        
        # y particionar recursivamente los elementos restantes en el arreglo


array = Array([5, 8, 2, 1, 9, 3, 7])
pivot = 4
print("Arreglo original:", array.items)

index = array.partition_rec(pivot)
print("Índice de partición:", index)
print("Arreglo después de la partición:", array.items)

