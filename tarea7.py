
def identity(x):
    return x  # Función de identidad

class PriorityQueue:
    def __init__(self, size, pri=identity):
        self.__maxSize = size
        self.__que = [None] * size
        self.__pri = pri
        self.__nItems = 0

    def insert(self, item):
        if self.isFull():
            raise Exception("Queue overflow")
        self.__que[self.__nItems] = item
        self.__nItems += 1
        return True

    def remove(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        max_priority = self.__pri(self.__que[0])
        max_index = 0
        for i in range(1, self.__nItems):
            priority = self.__pri(self.__que[i])
            if priority > max_priority:
                max_priority = priority
                max_index = i
        front = self.__que[max_index]
        for i in range(max_index, self.__nItems - 1):
            self.__que[i] = self.__que[i + 1]
        self.__que[self.__nItems - 1] = None
        self.__nItems -= 1
        return front

    def peek(self):
        return None if self.isEmpty() else self.__que[self.__nItems - 1]

    def isEmpty(self):
        return self.__nItems == 0

    def isFull(self):
        return self.__nItems == self.__maxSize

    def __len__(self):
        return self.__nItems

    def __str__(self):
        ans = "["
        for i in range(self.__nItems - 1, -1, -1):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__que[i])
        ans += "]"
        return ans


# Programa de prueba
if __name__ == "__main__":
    # Crear una instancia de PriorityQueue
    pq = PriorityQueue(5)

    # Insertar elementos en desorden
    pq.insert(4)
    pq.insert(2)
    pq.insert(6)
    pq.insert(1)

    # Mostrar el contenido de la cola de prioridad
    print(pq)

    # Eliminar elementos de mayor prioridad
    while not pq.isEmpty():
        print("Elemento de mayor prioridad:", pq.remove())