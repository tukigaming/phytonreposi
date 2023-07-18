class Array:
    def __init__(self, items):
        self.items = items
    def identity(x):
        return x
    def get(self, index):
        return self.items[index]

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def partition_rec(self, pivot, lo=0, hi=None, key=identity):
        if hi is None:
            hi = len(self.items) - 1

        while lo <= hi and key(self.get(lo)) < pivot:
            lo += 1

        while lo < hi and pivot < key(self.get(hi)):
            hi -= 1

        if lo >= hi:
            return lo

        self.swap(lo, hi)

        return self.partition_rec(pivot, lo + 1, hi - 1, key)


# Ejemplo de uso
array = Array([5, 8, 2, 1, 9, 3, 7])
pivot = 4
print("Arreglo original:", array.items)

index = array.partition_rec(pivot)
print("Índice de partición:", index)
print("Arreglo después de la partición:", array.items)
